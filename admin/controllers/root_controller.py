from flask import render_template, Blueprint, g, redirect, url_for, flash
from db.database import db
from common.models.post import Post
from forms.post import PostForm

root_bp = Blueprint('root_bp', __name__)

@root_bp.route('/', methods=['GET'])
def index():
    if not g.member:
        return redirect(url_for('login_bp.index'))

    form = PostForm()
    form.submit.label.text = '削除' # type: ignore
    posts = db.session.query(Post).filter(Post.is_deleted != True).all()
    return render_template('index.html', member=g.member, posts=posts, form=form)
