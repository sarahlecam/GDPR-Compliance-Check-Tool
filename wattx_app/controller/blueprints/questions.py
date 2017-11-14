from flask import jsonify, Blueprint, request, abort
from wattx_app.models.models import Questions
from wattx_app.models import db

bp = Blueprint('questions', __name__)

@bp.route('/', methods=['GET'])
def get_questions():
    if request.method == 'GET':
        qns = Questions.query.all()
        return jsonify([q.to_dict() for q in qns])

@bp.route("/<int:id1>", methods = ['GET'])
def get_question(id1):
    if request.method == 'GET':
        q = Questions.query.filter_by(order=id1).first()
        return jsonify(q.to_dict())
