from flask import jsonify, Blueprint, request, abort
from wattx_app.models.enterprise import Enterprise
from wattx_app.models import db

bp = Blueprint('api', __name__)

@bp.route("/enterprise/<int:id1>", methods=['GET', 'DELETE'])
def enterprise_view_id(id1):

    if request.method == 'GET':
        e = Enterprise.query.filter_by(company_id=id1).first()
        return jsonify(e.to_dict())

    elif request.method == 'DELETE':
        e = Enterprise.query.filter_by(company_id=id1).all()
        for object in e:
            db.session.delete(object)
        db.session.commit()
        return jsonify({'status': 'success'})

@bp.route("/enterprise/", methods=['POST', 'GET'])
def enterprise_view():
    if request.method == 'POST':
        if not request.json or not 'company_name' in request.json:
            abort(400)
        body = request.json

        e = Enterprise(company_id = body['company_id'], company_name=body['company_name'], data_type=body['data_type'], reason = body['reason'], shared = ['shared'])
        db.session.add(e)
        db.session.commit()

        return jsonify({
            'id': e.id
        })

    elif request.method == 'GET':
        enterprises = Enterprise.query.all()
        return jsonify([e.to_dict() for e in enterprises])
