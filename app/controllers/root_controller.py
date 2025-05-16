import requests
from flask import render_template, Blueprint

root_bp = Blueprint('root_bp', __name__)

@root_bp.route('/', methods=['GET'])
def index():
    response = requests.get('https://yehara.microcms.io/api/v1/blogs', headers={'X-MICROCMS-API-KEY': 'vkp24wfI3ZpvW1fZkS5OTxygmEAYYzJzG6y7'})
    data = response.json().get('contents', [])
    return render_template('index.html', data=data)
