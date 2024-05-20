#!/usr/bin/python3
"""
Python module for manipulating the content of a website
using the flask module
"""
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Routs traffic to the root of the website
    """
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
