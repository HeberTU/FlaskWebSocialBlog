# forms.py for Users
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import  ValidationError
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from puppycompanyblog.models import User


class LoginForm(FlaskForm):
    email StringField('Email: ', validators=[DataRequired(),Email()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Log In')

class Register(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired(),Email()])
    username = StringField('UserName: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired(), EqualTo('pass_confirm', message = 'Passwords must match.' )])
    pass_confirm = PasswordField('Confirm Password: ', validators=[DataRequired()])
