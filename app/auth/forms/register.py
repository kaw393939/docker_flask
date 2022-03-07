from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Regexp
from wtforms.fields import *

class register_form(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 150)])
    submit = SubmitField()