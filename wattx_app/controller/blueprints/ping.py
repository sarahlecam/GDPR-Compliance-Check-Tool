from flask import jsonify, Blueprint, request, current_app
from wattx_app.models.models import Questions, RecText
from wattx_app.controller.security import require_cookie
from itsdangerous import URLSafeTimedSerializer

bp = Blueprint('ping', __name__)

@bp.route('/')
def ping():
    return jsonify({'code': 'ping success!'})

@bp.route('/rectxt')
def rectxt():
    qns = RecText.query.all()
    return jsonify([q.to_dict() for q in qns])

@bp.route('/set_cookie')
def cookie_insertion():
    # redirect_to_index = redirect('/index')
    response = jsonify({"key":"cookiemonster"})#current_app.make_response(redirect_to_index )
    response.set_cookie('company_id',value='1')
    return response

@bp.route('/read_cookie')
@require_cookie
def read_cookie():
    # unserialize cookie payload
    key = current_app.config['SECRET_KEY']
    serializer = URLSafeTimedSerializer(secret_key = key)
    payload = request.cookies.get('CheckMateCookie')
    cookie_contents = serializer.loads(payload)
    return jsonify(cookie_contents)

@bp.route("/insecure", methods=['GET', 'POST'])
def ping_insecure():
    return jsonify({'code':'insecure ping success!'})

# @bp.route("/secure", methods=['GET', 'POST'])
# @requires_auth
# def ping_secure():
#     return jsonify({'code':'secure ping success!'})
