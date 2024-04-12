#!/usr/bin/env python3
"""Basic Flask_Babel setup with internationalization support
   Parametrize templates
   Force locale with URL parameter
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Determine the best match with our supported languages.
    """
    locale = request.args.get("locale")
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """render_template: 0-index.html
    """
    return render_template("3-index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
