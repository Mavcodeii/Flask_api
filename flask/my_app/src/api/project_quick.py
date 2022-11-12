from flask import Flask, Blueprint, jsonify
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres@localhost:5432/my_app',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SQLALCHEMY_ECHO=True
)

bp = Blueprint('project', __name__, url_prefix='/project_data')


@bp.route('', methods=['GET'])
def index():
    result = []
    engine = db.get_engine()
    with engine.connect() as conn:
        rows = conn.execute(
            'SELECT id, name FROM project_api;')
        for r in rows:
            result.append({'id': r[0], 'project name': r[1]})
    return jsonify(result)
