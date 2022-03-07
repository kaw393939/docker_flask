from flask import Blueprint, render_template, request, redirect, url_for
from app.auth.forms.login import login_form
from app.auth.forms.register import register_form

auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        return redirect(url_for('auth.dashboard'))
    else:
        form_login = login_form()
        return render_template('login.html', form=form_login)


@auth.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        return redirect(url_for('auth.login'))
    else:
        form_register = register_form()
        return render_template('register.html', form=form_register)


@auth.route('/dashboard/<username>', methods=['POST', 'GET'])
def dashboard(username):
    return render_template('dashboard.html', username=username )
