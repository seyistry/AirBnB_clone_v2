#!/usr/bin/python3
"""
List of states
"""
from models import storage
from models.state import State
from models.amenity import Amenity

from flask import Flask, render_template, abort

app = Flask(__name__)
app.url_map.strict_slashes = False
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route('/hbnb_filters')
def filter():
    """Run all states"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def do_teardown(self):
    """Closes session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
