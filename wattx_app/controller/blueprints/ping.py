from flask import jsonify, Blueprint, request
from wattx_app.models.models import Questions


bp = Blueprint('ping', __name__)

@bp.route('/')
def ping():
    return jsonify({'code': 'ping success!'})


@bp.route('/set_cookie')
def cookie_insertion():
    # redirect_to_index = redirect('/index')
    response = jsonify({"key":"cookiemonster"})#current_app.make_response(redirect_to_index )
    response.set_cookie('company_id',value='1')
    return response

@bp.route('/read_cookie')
def read_cookie():
    return request.cookies.get('company_id')

@bp.route("/insecure", methods=['GET', 'POST'])
def ping_insecure():
    return jsonify({'code':'insecure ping success!'})

# @bp.route("/secure", methods=['GET', 'POST'])
# @requires_auth
# def ping_secure():
#     return jsonify({'code':'secure ping success!'})
