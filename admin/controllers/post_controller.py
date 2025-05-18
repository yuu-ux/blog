from flask import Blueprint, redirect, url_for, render_template, request, g, flash
from db.database import db
from models.post import Post
from forms.post import PostForm
from sqlalchemy.exc import SQLAlchemyError
import logging


post_bp = Blueprint('post_bp', __name__)

@post_bp.route('/<int:post_id>', methods=['GET'])
def index(post_id):
    if not g.member:
        return redirect(url_for('login_bp.index'))

    post = db.session.query(Post).filter(Post.id == post_id, Post.is_deleted != True).first()
    if post is None:
        flash('記事を取得できませんでした', 'error')
        return redirect('root_bp.index')
    return render_template('posts/index.html', member=g.member, post=post)

@post_bp.route('/<int:post_id>/edit', methods=['GET', 'POST']) #type: ignore
def edit(post_id):
    if not g.member:
        return redirect(url_for('login_bp.index'))

    post = db.session.query(Post).filter(Post.id == post_id, Post.is_deleted != True).first()
    if post is None:
        flash('記事を取得できませんでした', 'error')
        logging.error('error get post')
        return redirect('root_bp.index')

    form = PostForm()
    if request.method == 'GET':
        form.title.data = post.title # type: ignore
        form.body.data = post.body # type: ignore

    if form.validate_on_submit():
        try:
            post.title = form.title.data # type: ignore
            post.body = form.body.data # type: ignore
            db.session.commit()
        except SQLAlchemyError:
            logging.error('error post edit')
            flash('記事の更新に失敗しました', 'error')
            return redirect(url_for('post_bp.index', post_id=post.id))
        flash('記事を更新しました', 'info')
        return redirect(url_for('post_bp.index', post_id=post.id))

    return render_template('posts/edit.html', member=g.member, post=post, form=form)
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
