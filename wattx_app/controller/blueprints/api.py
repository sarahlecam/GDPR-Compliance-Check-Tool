from flask import jsonify, Blueprint, request, abort
from wattx_app.models.models import Users, Questions, Responses
from wattx_app.models import db

bp = Blueprint('api', __name__)

# User information
@bp.route("/users", methods=['POST', 'GET'])
def enterprise_view():


    if request.method == 'POST':

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

    elif request.method == 'GET':
        # TODO: return user based on cookie
        # Get company_id from cookie
        c_id_from_cookie = int(request.cookies.get('company_id'))
        usr = Users.query.filter(Users.company_id == c_id_from_cookie).first()
        return jsonify(usr.to_dict())

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



@bp.route("/recs", methods = ['GET'])
def get_recs():
    if request.method == 'GET':

        # Get company_id from cookie
        c_id_from_cookie = int(request.cookies.get('company_id'))
        # Get distinct section numbers from Questions table
        distinct_sec_nums = [s[0] for s in db.session.query(Questions.section).distinct()]
        print("Distinct sec nums: ", distinct_sec_nums)
        # Loop through each section
        for value in distinct_sec_nums:
            # Get distinct question id's
            distinct_questions = [q[0] for q in db.session.query(Questions.order).filter(Questions.section == value).distinct()]
            resp_vec = []
            # Generate corresponding responses for each question id
            for i in distinct_questions:
                v = Responses.query.filter(Responses.question_id == i).filter(Responses.company_id== c_id_from_cookie)
                resp_vec += [y.to_dict() for y in v]
            print("Vec: ", resp_vec)
            resp_sum = 0
            # Logic to determine recommendation based on each response in the section
            for j in resp_vec:
                # Arbitrary criteria for a decision
                if j['response'] != 'Yes.':
                    resp_sum += 1
            print("Resp_sum: ", resp_sum)
            # Add to Recommendations table




        rspns = Responses.query.filter_by(company_id = c_id_from_cookie)
        res_list = [r.to_dict() for r in rspns]
        for i in range(len(res_list)):
            print(res_list[i])

        return jsonify([r.to_dict() for r in rspns])






#
#
