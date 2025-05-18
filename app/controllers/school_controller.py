from flask import render_template, Blueprint
from common.db.database import db
from common.models.post import Post

school_bp = Blueprint('school_bp', __name__)


@school_bp.route('/', methods=['GET'])
def index():
    posts = db.session.query(Post).filter(Post.category_id == 2).all()
    return render_template('school/index.html', posts=posts)
