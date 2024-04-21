#!/usr/bin/python3
"""Flask web application starter"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """'Hello HBNB!' displayed"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
