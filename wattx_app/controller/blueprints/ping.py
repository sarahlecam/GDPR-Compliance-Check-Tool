from flask import jsonify, Blueprint, request
from wattx_app.models.models import Questions


bp = Blueprint('ping', __name__)

@bp.route('/')
def ping():
    return jsonify({'code': 'ping success!'})

@bp.route('/questions', methods=['GET'])
def get_questions():
    if request.method == 'GET':
        qns = Questions.query.all()
        return jsonify([q.to_dict() for q in qns])

@bp.route("/insecure", methods=['GET', 'POST'])
def ping_insecure():
    return jsonify({'code':'insecure ping success!'})

# @bp.route("/secure", methods=['GET', 'POST'])
# @requires_auth
# def ping_secure():
#     return jsonify({'code':'secure ping success!'})
