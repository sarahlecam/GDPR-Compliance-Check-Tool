from flask import jsonify, Blueprint, request, abort
from wattx_app.models.models import Users, Questions, Responses, RecText, Recommendations
from wattx_app.controller.security import require_cookie
from wattx_app.controller.recommend_logic import rec_logic
from wattx_app.models import db
from sqlalchemy.sql.expression import func

bp = Blueprint('api', __name__)

# User information
@bp.route("/users", methods = ['GET'])
@require_cookie
def get_user():
    # Get company_id from cookie
    c_id_from_cookie = int(request.cookies.get('company_id'))
    usr = Users.query.filter(Users.company_id == c_id_from_cookie).first()
    return jsonify(usr.to_dict())

@bp.route("/users", methods = ['POST'])
def enterprise_view():

    print('-'*50)
    print(request.data)
    print('-'*50)

    # Extract body from request
    body = request.json

    if not request.json or not 'email' in request.json:
        abort(400)

    # if it already exists in the database
    if (Users.query.filter_by(email=body['email']).count() > 0):
        e = Users.query.filter_by(email=body['email']).first()
    # otherwise create a new entry for it
    else:
        e = Users(
        company_name = body['company_name'],
        email = body['email'],
        password = body['password']
        )

        db.session.add(e)
        db.session.commit()


    # Return company id
    r = jsonify(e.to_dict())
    r.set_cookie('company_id', value = str(e.company_id))
    return r


# Questions
@bp.route('/questions', methods=['GET'])
def get_questions():
    if request.method == 'GET':
        qns = Questions.query.all()
        return jsonify([q.to_dict() for q in qns])

# Get individual question
@bp.route("/questions/<int:id1>", methods = ['GET'])
def get_question(id1):
    if request.method == 'GET':
        q = Questions.query.filter_by(order=id1).first()
        return jsonify(q.to_dict())

# Handle responses
@bp.route("/responses", methods = ['GET', 'POST'])
@require_cookie
def get_responses():
    # Get company_id from cookie
    c_id_from_cookie = int(request.cookies.get('company_id'))

    if request.method == 'GET':
        rsps = Responses.query.filter_by(company_id = c_id_from_cookie).all()
        return jsonify([r.to_dict() for r in rsps])

    elif request.method == 'POST':
        body = request.json

        # if it already exists in the database
        if (Responses.query.filter(Responses.company_id==c_id_from_cookie).filter(Responses.question_id==body['question_id']).count() > 0):
            r = Responses.query.filter(Responses.company_id==c_id_from_cookie).filter(Responses.question_id==body['question_id']).first()
            r.response = body['response']
            db.session.commit()

            # Return jsonified Response object
            return jsonify(r.to_dict())

        # otherwise create a new entry for it
        else:

            print('-'*50)
            print(request.data)
            print('-'*50)

            r = Responses(
            question_id = body['question_id'],
            company_id = int(request.cookies.get('company_id')),
            response = body['response']
            )

            db.session.add(r)
            db.session.commit()

            # Return jsonified Response object
            return jsonify(r.to_dict())


@bp.route('/responses/<int:id1>', methods = ['GET'])
@require_cookie
def get_specific_resp(id1):
    # Get company_id from cookie
    c_id_from_cookie = int(request.cookies.get('company_id'))

    if request.method == 'GET':
        r = Responses.query.filter(Responses.company_id == c_id_from_cookie).filter(Responses.question_id == id1).first()
        return jsonify(r.to_dict())



@bp.route("/recs", methods = ['GET', 'POST'])
@require_cookie
def get_recs():
    # Get company_id from cookie
    c_id_from_cookie = int(request.cookies.get('company_id'))

    if request.method == 'GET':
        recs = Recommendations.query.filter_by(company_id = c_id_from_cookie).all()
        return jsonify([r.to_dict() for r in recs])

    if request.method == 'POST':

        # Get distinct section numbers from Questions table
        distinct_sec_nums = [s[0] for s in db.session.query(Questions.section).distinct()]

        # Max number of rectext entries
        max_recs = db.session.query(func.max(RecText.section)).one()

        # Loop through each section
        for sec in distinct_sec_nums:
            q = Questions.query.filter(Questions.section == sec).first()
            q_dict = q.to_dict()
            sec_name = q_dict['section_name']
            print("section, sec name: ", sec, sec_name)
            if sec <= int(max_recs[0]):
                resp_text, complete = rec_logic(c_id_from_cookie, sec)
                print("[api] Resp text: ", resp_text)
                # Add to recommendations table
                rcs = Recommendations(
                company_id = c_id_from_cookie,
                section = sec,
                section_name = sec_name,
                rec_text = resp_text,
                flagged = 0,
                completed = complete
                )

                # Add and commit
                db.session.add(rcs)
                db.session.commit()

        recs = Recommendations.query.filter(Recommendations.company_id == c_id_from_cookie).all()
        return jsonify([r.to_dict() for r in recs])






#
#
