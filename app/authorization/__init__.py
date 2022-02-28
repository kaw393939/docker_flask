from flask import Blueprint, render_template
from app.authorization.forms.login import login_form
from app.authorization.forms.register import register_form

authorization = Blueprint('authorization', __name__, template_folder='templates')


@authorization.route('/login')
def login_form_render():
    form_login = login_form()
    return render_template('login.html', form=form_login)

@authorization.route('/register')
def register_form_render():
    form_register = register_form()
    return render_template('register.html', form=form_register)
