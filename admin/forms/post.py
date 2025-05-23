from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('タイトル', validators=[DataRequired()])
    body = TextAreaField('本文')
    category = SelectField(
        'カテゴリ',
        choices=[(1, 'web'), (2, '42Tokyo')],
        coerce=int,
    )
    submit_publish = SubmitField()
    submit_delete = SubmitField('削除')
    submit_draft = SubmitField('下書き保存')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
