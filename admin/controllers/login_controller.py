from flask import Blueprint, render_template, url_for, redirect, flash
from forms.login import LoginForm
from db.database import db
from models.member import Member
from sqlalchemy.exc import SQLAlchemyError
import logging

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.name.data # type: ignore
        password = form.password.data # type: ignore
        try:
            member = db.session.query(Member).filter_by(name = name).first()
            if member is None or not Member.check_password(password, member.password):
                flash('ユーザー名またはパスワードが違います。', 'error')
                return redirect(url_for('login_bp.index'))
            else:
                Member.login(member)
                flash(f'{name}でログインしました')
                return redirect(url_for('root_bp.index'))
        except SQLAlchemyError:
            logging.exception('login error')
            form.name.data = '' # type: ignore
            form.password.data = '' # type: ignore
    return render_template('login.html', form=form)


