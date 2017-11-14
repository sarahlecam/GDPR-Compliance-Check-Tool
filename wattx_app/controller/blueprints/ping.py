from flask import jsonify, Blueprint, request
from wattx_app.models.models import Questions


bp = Blueprint('ping', __name__)

@bp.route('/')
def ping():
    return jsonify({'code': 'ping success!'})

@bp.route("/insecure", methods=['GET', 'POST'])
def ping_insecure():
    return jsonify({'code':'insecure ping success!'})

# @bp.route("/secure", methods=['GET', 'POST'])
# @requires_auth
# def ping_secure():
#     return jsonify({'code':'secure ping success!'})
