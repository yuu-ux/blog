from flask import render_template, Blueprint

web_bp = Blueprint('web_bp', __name__)

@web_bp.route('/', methods=['GET'])
def index():
    return render_template('web/index.html')
