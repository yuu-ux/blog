from flask import render_template, Blueprint
from common.db.database import db
from common.models.post import Post
from config import CATEGORY_WEB

web_bp = Blueprint('web_bp', __name__)


@web_bp.route('/', methods=['GET'])
def index():
    posts = db.session.query(Post).filter(Post.category_id == CATEGORY_WEB, Post.is_deleted != True).all()
    return render_template('web/index.html', posts=posts)
