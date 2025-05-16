from flask import render_template, Blueprint

school_bp = Blueprint('school_bp', __name__)

@school_bp.route('/', methods=['GET'])
def index():
    return render_template('school/index.html')
