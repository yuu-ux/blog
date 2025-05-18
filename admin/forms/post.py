from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('タイトル', validators=[DataRequired()])
    body = TextAreaField('本文')
    category = SelectField('カテゴリ', choices=[
        (1, 'web'),
        (2, '42Tokyo'),
    ], coerce=int)
    submit = SubmitField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
