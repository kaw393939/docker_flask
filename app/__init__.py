"""A simple flask web app"""
from flask import Flask, render_template
from app.context_processors import utility_text_processors
from app.simple_pages import simple_pages


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.register_blueprint(simple_pages)
    app.context_processor(utility_text_processors)

    return app
