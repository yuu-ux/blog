from flask import render_template, Blueprint, url_for, redirect, flash
from common.db.database import db
from common.models.post import Post
from config import CATEGORY_WEB

web_bp = Blueprint('web_bp', __name__)


@web_bp.route('/', methods=['GET'])
def index():
    posts = (
        db.session.query(Post)
        .filter(Post.category_id == CATEGORY_WEB, Post.is_deleted != True)
        .all()
    )
    return render_template('web/index.html', posts=posts)


@web_bp.route('/<int:post_id>', methods=['GET'])
def detail(post_id):
    post = (
        db.session.query(Post)
        .filter(Post.id == post_id, Post.is_deleted != True)
        .first()
    )
    if post is None:
        flash('記事が見つかりませんでした', 'error')
        return redirect(url_for('web_bp.index'))
    return render_template('web/detail.html', post=post)
