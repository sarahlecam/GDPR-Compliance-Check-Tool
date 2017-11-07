from flask import jsonify, Blueprint, request, abort, current_app, send_from_directory

bp = Blueprint('index', __name__)

@bp.route('/')
def serveIndex():
    return current_app.send_static_file('index.html')

@bp.route('/<path:filename>')
def serveImages(filename):
    return send_from_directory('static', filename)
