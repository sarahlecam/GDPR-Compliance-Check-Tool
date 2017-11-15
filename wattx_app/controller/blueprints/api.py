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

        if not request.json or not 'email' in request.json:
            abort(400)

        body = request.json

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
        return str(e.company_id)

    elif request.method == 'GET':
        users = Users.query.all()
        return jsonify([e.to_dict() for e in users])

# Questions
@bp.route('/questions', methods=['GET'])
def get_questions():
    if request.method == 'GET':
        qns = Questions.query.all()
        return jsonify([q.to_dict() for q in qns])

@bp.route("/questions/<int:id1>", methods = ['GET'])
def get_question(id1):
    if request.method == 'GET':
        q = Questions.query.filter_by(order=id1).first()
        return jsonify(q.to_dict())

@bp.route("/responses", methods = ['GET', 'POST'])
def get_responses():
    if request.method == 'GET':
        # Hard coding company id = 1.
        # TODO: Get company id from token or session or something?
        rsps = Responses.query.filter_by(company_id = 1).all()
        return jsonify([r.to_dict() for r in rsps])

    elif request.method == 'POST':
        body = request.json

        print(body)
        r = Responses(
        question_id = body['question_id'],
        company_id = body['company_id'],
        response = body['response']
        )

        db.session.add(r)
        db.session.commit()


    # Return company id
    return str(r.company_id) + "," + str(r.question_id)


# Change information about an existing company
# @bp.route("/enterprise/<int:id1>", methods=['PUT', 'GET', 'DELETE'])
# def enterprise_view_id(id1):
#     if request.method == 'PUT':
#
#         # TODO: Needs to be tested!
#
#         print('-'*50)
#         print(request.data)
#         print('-'*50)
#
#         if not request.json or not 'data_type' in request.json:
#             abort(400)
#
#         body = request.json
#
#         e = EnterpriseData.query.filter_by(company_id=id1).first()
#         if 'company_name' in body and body['company_name'] != e.company_name:
#             e.company_name = body['company_name']
#         if 'address' in body and body['address'] != e.address:
#             e.address = body['address']
#         if 'contact' in body and body['contact'] != e.contact:
#             e.contact = body['contact']
#         if 'website' in body and body['website'] != e.website:
#             e.website = body['website']
#         if 'dpo_name' in body and body['dpo_name'] != e.dpo_name:
#             e.dpo_name = body['dpo_name']
#         if 'dpo_contact' in body and body['dpo_contact'] != e.dpo_contact:
#             e.company_name = body['company_name']
#
#         db.session.add(e)
#         db.session.commit()
#
#         return jsonify({
#             'company_id': e.company_id
#         })
#
#     if request.method == 'GET':
#         e_data = EnterpriseData.query.filter_by(company_id=id1).all()
#         return jsonify([e.to_dict() for e in e_data])
#
#     elif request.method == 'DELETE':
#         e = EnterpriseData.query.filter_by(company_id=id1).all()
#         for object in e:
#             db.session.delete(object)
#         db.session.commit()
#         return jsonify({'status': 'success'})


# @bp.route("/enterprise/<int:id>/data", methods = ['POST', 'GET'])
# def enterprise_view_id_data(id):
#
#     if request.method == 'POST':
#
#         print('-'*50)
#         print(request.data)
#         print('-'*50)
#
#         if not request.json or not 'data_type' in request.json:
#             abort(400)
#
#         body = request.json
#
#         e = EnterpriseData(
#             company_id = id,
#             data_type=body['data_type'],
#             reason = body['reason'],
#             shared = body['shared']
#         )
#         db.session.add(e)
#         db.session.commit()
#
#         return jsonify({
#             'id': e.id
#         })
#
#     # Shouldn't need to use this. Just for debugging.
#     # Gets all EnterpriseData entries despite company id.
#     if request.method == 'GET':
#         enterprises = EnterpriseData.query.all()
#         return jsonify([e.to_dict() for e in enterprises])
