from flask import Blueprint, redirect, url_for, render_template, session, g, flash
from db.database import db
from models.post import Post
from forms.post import PostForm


post_bp = Blueprint('post_bp', __name__)

@post_bp.route('/<int:post_id>', methods=['GET'])
def index(post_id):
    if not g.member:
        return redirect(url_for('login_bp.index'))

    form = PostForm()
    post = db.session.get(Post, post_id)
    if post is None:
        flash('記事を取得できませんでした', 'error')
        return redirect('root_bp.index')
    return render_template('posts/index.html', member=g.member, post=post, form=form)

# @post_bp.route('/<int:post_id>/edit', methods=['GET', 'POST'])
# def edit(post_id):
#     if not g.member:
#         return redirect(url_for('login_bp.index'))
#
#     form = PostForm()
#     post = db.session.get(Post, post_id)
#     if post is None:
#         return
#     form.body.data = post.data
#     if not form.validate_on_submit():
#         return redirect('post_bp.detail')
#
#     post = db.session.get(Post, post_id)
#     post.body = input
#     db.session.commit()
#     flash('記事を更新しました', 'info')
#     return redirect(url_for('post_bp.detail'))
#
#
# @post_bp.route('/delete/<int:post_id>', methods=['POST'])
# def delete(post_id):
#     if not g.member:
#         return redirect(url_for('login_bp.index'))
#     post = db.session.get(Post, post_id)
#     if post is None:
#         flash('記事の削除に失敗しました', 'error')
#         return redirect(url_for('post_bp.index'))
#     post.is_deleted = True
#     db.session.commit()
#     flash('記事を削除しました', 'info')
#     return redirect(url_for('post_bp.index'))
