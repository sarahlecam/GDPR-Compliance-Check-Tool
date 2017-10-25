from flask import jsonify, Blueprint, request, abort, current_app

bp = Blueprint('index', __name__)

@bp.route('')
def serveIndex():
    return current_app.send_static_file('index.html')
