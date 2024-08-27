#!/usr/bin/env python3
""" Flask application module """
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """ Flask app configuration class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route("/")
def home():
    """ Home route """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
