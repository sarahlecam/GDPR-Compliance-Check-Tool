from flask import jsonify, Blueprint, request, abort, current_app
from wattx_app.models.models import Users, Questions, Responses, RecText, Recommendations
from wattx_app.controller.security import require_cookie
from wattx_app.controller.recommend_logic import rec_logic
from wattx_app.models import db
from sqlalchemy.sql.expression import func
import bcrypt
from itsdangerous import URLSafeTimedSerializer

bp = Blueprint('api', __name__)

# User information
@bp.route("/users", methods = ['GET'])
# @require_cookie
def get_user():
    usrs = Users.query.all()
    return jsonify([u.to_dict() for u in usrs])
    ###########


    # # Get company_id from cookie
    # c_id_from_cookie = int(request.cookies.get('company_id'))
    # usr = Users.query.filter(Users.company_id == c_id_from_cookie).first()
    # return jsonify(usr.to_dict())

# TODO: This needs to be SIGNUP
@bp.route("/users/signup", methods = ['POST'])
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
        password = bcrypt.hashpw(body['password'].encode('utf-8'), bcrypt.gensalt(10)) # bcrypt hashed password
        )

        db.session.add(e)
        db.session.commit()

    # Create cookie
    e_dict = e.to_dict()
    key = current_app.config['SECRET_KEY']
    # make payload with itsdangerous.URLSafeTimedSerializer
    serializer = URLSafeTimedSerializer(secret_key = key)
    cookie_data = {
        'company_id': e_dict['company_id'],
        'company_name': e_dict['company_name']
    }
    payload = serializer.dumps(cookie_data)
    r = jsonify({'Login': 'Login successful'})
    # put that payload in cookie on user's browser
    r.set_cookie('CheckMateCookie', value = payload)
    return r

@bp.route('/users/login', methods=['POST'])
def login_view():

    # get username/password from body json
    body = request.json
    print(body)
    # get user object from database
        # if user doesn't exist, abort(401)
    if (Users.query.filter_by(email=body['email']).count() > 0):
        usr = Users.query.filter_by(email=body['email']).first()
        usr_dict = usr.to_dict()
    else:
        abort(401)

    # check inbound password against user.password with bcrypt.checkpwd
    # Get hashed pw from user object
    hashed_pw = usr_dict['password'].encode('utf-8')
    inbound_pw = body['password'].encode('utf-8')
    if bcrypt.checkpw(inbound_pw, hashed_pw):
        # It matches, make them a cookie
        key = current_app.config['SECRET_KEY']
        # make payload with itsdangerous.URLSafeTimedSerializer
        serializer = URLSafeTimedSerializer(secret_key = key)
        cookie_data = {
            'company_id': usr_dict['company_id'],
            'company_name': usr_dict['company_name']
        }
        payload = serializer.dumps(cookie_data)
        r = jsonify({'Login': 'Login successful'})
        # put that payload in cookie on user's browser
        r.set_cookie('CheckMateCookie', value = payload)
        # return good status
        return r
    else:
        # It does not match, don't make a cookie
        r = jsonify({'Login error': 'Email and/or password do not match'})
        r.status_code = 401
        # return bad status
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
    key = current_app.config['SECRET_KEY']
    serializer = URLSafeTimedSerializer(secret_key = key)
    payload = request.cookies.get('CheckMateCookie')
    cookie_contents = serializer.loads(payload)
    c_id_from_cookie = int(cookie_contents['company_id'])

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
            company_id = c_id_from_cookie,
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
    key = current_app.config['SECRET_KEY']
    serializer = URLSafeTimedSerializer(secret_key = key)
    payload = request.cookies.get('CheckMateCookie')
    cookie_contents = serializer.loads(payload)
    c_id_from_cookie = int(cookie_contents['company_id'])

    if request.method == 'GET':
        r = Responses.query.filter(Responses.company_id == c_id_from_cookie).filter(Responses.question_id == id1).first()
        return jsonify(r.to_dict())



@bp.route("/recs", methods = ['GET', 'POST'])
@require_cookie
def get_recs():
    # Get company_id from cookie
    key = current_app.config['SECRET_KEY']
    serializer = URLSafeTimedSerializer(secret_key = key)
    payload = request.cookies.get('CheckMateCookie')
    cookie_contents = serializer.loads(payload)
    c_id_from_cookie = int(cookie_contents['company_id'])

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
            if sec <= int(max_recs[0]):
                resp_text, complete = rec_logic(c_id_from_cookie, sec)
                # If rec exists, update it.
                if (Recommendations.query.filter(Recommendations.company_id == c_id_from_cookie)\
                .filter(Recommendations.section == sec).count() > 0):
                    rec = Recommendations.query.filter(Recommendations.company_id == c_id_from_cookie)\
                    .filter(Recommendations.section == sec).first()
                    rec.section_name = sec_name
                    rec.rec_text = resp_text
                    rec.flagged = 0
                    rec.completed = 0

                    # Add session
                    db.session.add(rec)
                else:
                    # Add to recommendations table
                    rcs = Recommendations(
                    company_id = c_id_from_cookie,
                    section = sec,
                    section_name = sec_name,
                    rec_text = resp_text,
                    flagged = 0,
                    completed = complete
                    )
                    # Add session
                    db.session.add(rcs)
                # Commit session
                db.session.commit()

        recs = Recommendations.query.filter(Recommendations.company_id == c_id_from_cookie).all()
        return jsonify([r.to_dict() for r in recs])

@bp.route("/recs/<int:id1>", methods = ['POST'])
@require_cookie
def update_rec(id1):
    # Get company_id from cookie
    key = current_app.config['SECRET_KEY']
    serializer = URLSafeTimedSerializer(secret_key = key)
    payload = request.cookies.get('CheckMateCookie')
    cookie_contents = serializer.loads(payload)
    c_id_from_cookie = int(cookie_contents['company_id'])

    # Get request body
    body = request.json

    # Update rec with contents of body
    rec = Recommendations.query.filter(Recommendations.company_id == c_id_from_cookie)\
    .filter(Recommendations.section == id1).first()
    if 'flagged' in body:
        rec.flagged = body['flagged']
    if 'completed' in body:
        rec.completed = body['completed']

    # Commit session
    db.session.commit()

    # Return jsonified Recommendations object
    return jsonify(rec.to_dict())


@bp.route("/recs/filter/", methods=['GET'])
@require_cookie
def filter_recs():
    # Get company_id from cookie
    key = current_app.config['SECRET_KEY']
    serializer = URLSafeTimedSerializer(secret_key = key)
    payload = request.cookies.get('CheckMateCookie')
    cookie_contents = serializer.loads(payload)
    c_id_from_cookie = int(cookie_contents['company_id'])

    # Get request args
    flagged_setting = request.args.get('flagged')
    print("Flagged setting: ", flagged_setting)
    completed_setting = request.args.get('completed')
    print("Completed setting: ", completed_setting)

    if flagged_setting is not None and completed_setting is not None:
        recs = Recommendations.query.filter(Recommendations.company_id == c_id_from_cookie)\
        .filter(Recommendations.flagged == flagged_setting)\
        .filter(Recommendations.completed == completed_setting).all()
    elif flagged_setting is not None:
        recs = Recommendations.query.filter(Recommendations.company_id == c_id_from_cookie)\
        .filter(Recommendations.flagged == flagged_setting).all()
    elif completed_setting is not None:
        recs = Recommendations.query.filter(Recommendations.company_id == c_id_from_cookie)\
        .filter(Recommendations.completed == completed_setting).all()
    else:
        r = jsonify({'Handling error': 'No parameters supplied'})
        r.status_code = 400
        return r
    return jsonify([r.to_dict() for r in recs])



#
#
