import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, jsonify
db = SQLAlchemy()
# Reference:
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
# https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.Column
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#many-to-many-relationships

bp = Blueprint('project', __name__, url_prefix='/project_data')


@bp.route('', methods=['GET'])
def index():
    result = []
    engine = db.get_engine()
    with engine.connect() as conn:
        rows = conn.execute(
            'SELECT id, name FROM project;')
        for r in rows:
            result.append({'id': r[0], 'project name': r[1]})
    return jsonify(result)


# TODO add a function for all the data to be returned **Need to update the for loop on line 20


@bp.route('/str: name/', methods=['GET'])
def index(name):
    result = []
    engine = db.get_engine()
    with engine.connect() as conn:
        rows = conn.execute(
            'SELECT * FROM project_api Where name =' + name + ';')
        for r in rows:
            result.append({'id': r[0], 'project name': r[1]

                           })
    return jsonify(result)
