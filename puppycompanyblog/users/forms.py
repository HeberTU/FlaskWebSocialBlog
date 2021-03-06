# forms.py for Users
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import  ValidationError
from flask_wtf.file import FileField, FileAllowed

from flask_login import login_required ,current_user
from puppycompanyblog.models import User


class LoginForm(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired(),Email()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired(),Email()])
    username = StringField('UserName: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired(), EqualTo('pass_confirm', message = 'Passwords must match.' )])
    pass_confirm = PasswordField('Confirm Password: ', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(f'{field.data} has been registered')
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(f'{field.data} has been registered')


class UpdateForm(FlaskForm):
    email = StringField('Email: ', validators = [DataRequired(),Email()])
    username = StringField('UserName: ', validators = [DataRequired()])
    picture = FileField('Choose file...', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(f'{field.data} has been registered')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(f'{field.data} has been registered')
