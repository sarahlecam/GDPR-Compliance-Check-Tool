from flask import jsonify, Blueprint, request, abort
from wattx_app.models.models import Enterprise, EnterpriseData, Questions
from wattx_app.models import db

bp = Blueprint('api', __name__)

# Input information
@bp.route("/enterprise/", methods=['POST', 'GET'])
def enterprise_view():
    if request.method == 'POST':

        print('-'*50)
        print(request.data)
        print('-'*50)

        if not request.json or not 'company_name' in request.json:
            abort(400)

        body = request.json

        # if it already exists in the database
        if (Enterprise.query.filter_by(company_name=body['company_name']).count() > 0):
            e = Enterprise.query.filter_by(company_name=body['company_name']).first()
        # otherwise create a new entry for it
        else:
            e = Enterprise(
            company_name = body['company_name'],
            address=body['address'],
            contact = body['contact'],
            website = body['website'],
            dpo_name = body['dpo_name'],
            dpo_contact = body['dpo_contact'],
            company_type = body['company_type']
            )

            db.session.add(e)
            db.session.commit()


        # Return company id
        return str(e.company_id)

    elif request.method == 'GET':
        enterprises = Enterprise.query.all()
        return jsonify([e.to_dict() for e in enterprises])



# Change information about an existing company
@bp.route("/enterprise/<int:id1>", methods=['PUT', 'GET', 'DELETE'])
def enterprise_view_id(id1):
    if request.method == 'PUT':

        # TODO: Needs to be tested!

        print('-'*50)
        print(request.data)
        print('-'*50)

        if not request.json or not 'data_type' in request.json:
            abort(400)

        body = request.json

        e = EnterpriseData.query.filter_by(company_id=id1).first()
        if 'company_name' in body and body['company_name'] != e.company_name:
            e.company_name = body['company_name']
        if 'address' in body and body['address'] != e.address:
            e.address = body['address']
        if 'contact' in body and body['contact'] != e.contact:
            e.contact = body['contact']
        if 'website' in body and body['website'] != e.website:
            e.website = body['website']
        if 'dpo_name' in body and body['dpo_name'] != e.dpo_name:
            e.dpo_name = body['dpo_name']
        if 'dpo_contact' in body and body['dpo_contact'] != e.dpo_contact:
            e.company_name = body['company_name']

        db.session.add(e)
        db.session.commit()

        return jsonify({
            'company_id': e.company_id
        })

    if request.method == 'GET':
        e_data = EnterpriseData.query.filter_by(company_id=id1).all()
        return jsonify([e.to_dict() for e in e_data])

    elif request.method == 'DELETE':
        e = EnterpriseData.query.filter_by(company_id=id1).all()
        for object in e:
            db.session.delete(object)
        db.session.commit()
        return jsonify({'status': 'success'})


@bp.route("/enterprise/<int:id>/data", methods = ['POST', 'GET'])
def enterprise_view_id_data(id):

    if request.method == 'POST':

        print('-'*50)
        print(request.data)
        print('-'*50)

        if not request.json or not 'data_type' in request.json:
            abort(400)

        body = request.json

        e = EnterpriseData(
            company_id = id,
            data_type=body['data_type'],
            reason = body['reason'],
            shared = body['shared']
        )
        db.session.add(e)
        db.session.commit()

        return jsonify({
            'id': e.id
        })

    # Shouldn't need to use this. Just for debugging.
    # Gets all EnterpriseData entries despite company id.
    if request.method == 'GET':
        enterprises = EnterpriseData.query.all()
        return jsonify([e.to_dict() for e in enterprises])
