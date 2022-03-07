"""A simple flask web app"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

from app.context_processors import utility_text_processors
from app.simple_pages import simple_pages
from app.auth import auth
from app.exceptions import http_exceptions

def page_not_found(e):
    return render_template("404.html"), 404

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    bootstrap = Bootstrap5(app)
    app.register_blueprint(simple_pages)
    app.register_blueprint(auth)
    app.context_processor(utility_text_processors)
    app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'flatly'
    app.register_error_handler(404,page_not_found)
    #app.add_url_rule("/", endpoint="index")

    return app
