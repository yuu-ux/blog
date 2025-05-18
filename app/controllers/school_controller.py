from flask import render_template, Blueprint
from common.db.database import db
from common.models.post import Post
from config import CATEGORY_SCHOOL

school_bp = Blueprint('school_bp', __name__)


@school_bp.route('/', methods=['GET'])
def index():
    posts = db.session.query(Post).filter(Post.category_id == CATEGORY_SCHOOL, Post.is_deleted != True).all()
    return render_template('school/index.html', posts=posts)
