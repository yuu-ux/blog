from flask import render_template, Blueprint
from common.db.database import db
from common.models.post import Post

web_bp = Blueprint('web_bp', __name__)

@web_bp.route('/', methods=['GET'])
def index():
    posts = db.session.query(Post).filter(Post.category_id == 1).all()
    return render_template('web/index.html', posts=posts)
