from flask import render_template, Blueprint, g, redirect, url_for, flash
from db.database import db
from models.post import Post

root_bp = Blueprint('root_bp', __name__)

@root_bp.route('/', methods=['GET'])
def index():
    if not g.member:
        return redirect(url_for('login_bp.index'))

    posts = db.session.query(Post).filter(Post.is_deleted != True).all()
    return render_template('index.html', member=g.member, posts=posts)

@root_bp.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    if not g.member:
        return redirect(url_for('login_bp.index'))
    post = db.session.query(Post).filter_by(id = post_id).first()
    if post is None:
        flash('記事の削除に失敗しました', 'error')
        return redirect(url_for('root_bp.index'))
    post.is_deleted = True
    db.session.commit()
    flash('記事を削除しました', 'info')
    return redirect(url_for('root_bp.index'))

