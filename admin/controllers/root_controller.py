from flask import render_template, Blueprint

root_bp = Blueprint('root_bp', __name__)

@root_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

