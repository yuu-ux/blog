from flask import Blueprint, redirect, url_for, render_template, request, g, flash
from common.db.database import db
from common.models.post import Post
from forms.post import PostForm
from sqlalchemy.exc import SQLAlchemyError
import logging


post_bp = Blueprint('post_bp', __name__)


@post_bp.route('/<int:post_id>', methods=['GET'])
def index(post_id):
    if not g.member:
        return redirect(url_for('login_bp.index'))

    post = (
        db.session.query(Post)
        .filter(Post.id == post_id, Post.is_deleted != True)
        .first()
    )
    if post is None:
        flash('記事を取得できませんでした', 'error')
        return redirect('root_bp.index')
    return render_template('posts/index.html', member=g.member, post=post)


@post_bp.route('/create', methods=['GET', 'POST'])
def create():
    if not g.member:
        return redirect(url_for('login_bp.index'))

    form = PostForm()
    form.submit_publish.label.text = '作成'  # type: ignore

    if form.validate_on_submit():
        if Post.save_post(form) is None:
            flash('記事が作成できませんでした', 'error')
            return redirect(url_for('post_bp.create'))

        flash('記事を作成しました', 'info')
        return redirect(url_for('root_bp.index'))
    return render_template('posts/edit.html', member=g.member, form=form)


@post_bp.route('/<int:post_id>/edit', methods=['GET', 'POST'])
def edit(post_id):
    if not g.member:
        return redirect(url_for('login_bp.index'))

    post = (
        db.session.query(Post)
        .filter(Post.id == post_id, Post.is_deleted != True)
        .first()
    )
    if post is None:
        flash('記事を取得できませんでした', 'error')
        logging.error('error get post')
        return redirect('root_bp.index')

    form = PostForm()
    form.submit_publish.label.text = '更新'  # type: ignore
    if request.method == 'GET':
        form.title.data = post.title  # type: ignore
        form.body.data = post.body  # type: ignore

    if form.validate_on_submit():
        if Post.save_post(form, post) is None:
            flash('記事の更新に失敗しました', 'error')
            return redirect(url_for('post_bp.index', post_id=post.id))

        flash('記事を更新しました', 'info')
        return redirect(url_for('post_bp.index', post_id=post.id))

    return render_template('posts/edit.html', member=g.member, post=post, form=form)


@post_bp.route('/<int:post_id>/publish', methods=['POST'])
def publish(post_id):
    if not g.member:
        return redirect(url_for('login_bp.index'))

    post = (
        db.session.query(Post)
        .filter(Post.id == post_id, Post.is_deleted != True)
        .first()
    )
    if post.publish_post() is None:
        flash('投稿できませんでした', 'error')

    return redirect(url_for('root_bp.index'))


@post_bp.route('/<int:post_id>/delete', methods=['POST'])
def delete(post_id):
    if not g.member:
        return redirect(url_for('login_bp.index'))

    post = (
        db.session.query(Post)
        .filter(Post.id == post_id, Post.is_deleted != True)
        .first()
    )
    if post is None:
        flash('存在しない記事です', 'error')
        logging.error('error post delete')
        return redirect(url_for('root_bp.index'))

    try:
        post.is_deleted = True  # type: ignore
        db.session.commit()
    except SQLAlchemyError:
        logging.exception('error post delete')
        flash('記事が削除できませんでした')
        return redirect(url_for('root_bp.index'))

    flash('記事を削除しました', 'info')
    return redirect(url_for('root_bp.index'))
