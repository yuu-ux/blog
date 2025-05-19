from flask import render_template, Blueprint, redirect, url_for, flash
from common.db.database import db
from common.models.post import Post
from config import CATEGORY_SCHOOL

school_bp = Blueprint('school_bp', __name__)


@school_bp.route('/', methods=['GET'])
def index():
    posts = (
        db.session.query(Post)
        .filter(Post.category_id == CATEGORY_SCHOOL, Post.is_deleted != True)
        .all()
    )
    return render_template('school/index.html', posts=posts)


@school_bp.route('/<int:post_id>', methods=['GET'])
def detail(post_id):
    post = (
        db.session.query(Post)
        .filter(Post.id == post_id, Post.is_deleted != True)
        .first()
    )
    if post is None:
        flash('記事が見つかりませんでした', 'error')
        return redirect(url_for('school_bp.index'))
    return render_template('includes/post.html', post=post)
