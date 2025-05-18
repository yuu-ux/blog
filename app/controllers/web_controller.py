from flask import render_template, Blueprint
from db.database import db

web_bp = Blueprint('web_bp', __name__)

@web_bp.route('/', methods=['GET'])
def index():
    articles = [
        {'id': 1, 'title': 'Using Flask with Docker', 'summary': 'A guide to containerizing your Flask app.'},
        {'id': 2, 'title': 'Intro to Echo Framework', 'summary': 'Why Echo is a great choice for lightweight APIs.'},
    ]
    return render_template('web/index.html', articles=articles)
