from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import *


class login_form(FlaskForm):
    email = EmailField('Email Address')
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.length(min=6,max=35)
    ])
    submit = SubmitField()


class register_form(FlaskForm):
    email = EmailField('Email Address')
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match'),
        validators.length(min=6,max=35)
    ])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField()