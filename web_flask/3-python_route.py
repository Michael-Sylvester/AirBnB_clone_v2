#!/usr/bin/python3
"""
Python module for manipulating the content of a website
using the flask module
"""
from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Routs traffic to the root of the website
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_page():
    """
    Routs traffic to hbhn page
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_page(text):
    """
    Routs traffic to display text on the c page
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_page(text="is cool"):
    """
    Routs traffic to display text on the python page
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')