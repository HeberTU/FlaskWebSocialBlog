from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class BlogPostForm(FlaskForm):

    titel = StringField('Tilte: ', validators=[DataRequired()])
    text = TextAreaField('Text: ', validators=DataRequired())
    submit = SubmitField('Post')
