#!/usr/bin/python3
"""Flask web application starts
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Main HBnB displayd filters HTML page."""
    states = storage.all("State")
    places = storage.all("Place")
    amenities = storage.all("Amenity")
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(exc):
    """Current SQLAlchemy session removd"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
