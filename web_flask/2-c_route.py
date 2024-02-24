#!/usr/bin/python3
"""Flask web application startd"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """'Hello HBNB!' displayd"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """'HBNB' displayd"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """'C' displayd followed by value of <text>"""
    txt = text.replace("_", " ")
    return "C {}".format(txt)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
