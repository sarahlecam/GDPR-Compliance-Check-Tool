from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import csv
from . import controller
from . import models
from wattx_app.models.models import Questions, RecText


def create_app():
    '''factory for flask app object'''

    # create app object
    app = Flask(__name__, static_folder='static')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 20
    # app.config['STATIC_FOLDER']='static'
    models.db.init_app(app)

    # register blueprints on app
    app.register_blueprint(controller.blueprints.ping.bp, url_prefix='/ping')
    app.register_blueprint(controller.blueprints.api.bp, url_prefix='/api')
    app.register_blueprint(controller.blueprints.index.bp, url_prefix='')

    # return app
    return app

def reset_db():
    '''drop and recreate all tables'''
    app=create_app()
    models.db.drop_all(app=app)
    models.db.create_all(app=app)


def import_questions(filename):
    app = create_app()
    with open(filename, newline='') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        with app.app_context():

            for row in reader:
                try:
                    descval = row[5]
                except IndexError:
                    descval = 'null'
                q = Questions(
                question = row[0],
                response_type = row[1],
                order = row[2],
                section = row[3],
                section_name = row[4],
                description = descval
                )
                models.db.session.add(q)
            models.db.session.commit()


def import_recs(filename):
    app = create_app()
    with open(filename, newline='') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        with app.app_context():
            for row in reader:
                rt = RecText(
                rec_text = row[0].strip(),
                section = row[1],
                completed = row[2]
                )
                models.db.session.add(rt)
            models.db.session.commit()
