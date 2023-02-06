#!/usr/bin/python3
"""
List of states
"""
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User

from flask import Flask, render_template, abort

app = Flask(__name__)
app.url_map.strict_slashes = False
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route('/hbnb')
def filter():
    """Run all states"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    user = storage.all(User)
    return render_template('100-hbnb.html',
                           states=states,
                           amenities=amenities,
                           places=places,
                           user=user)


@app.teardown_appcontext
def do_teardown(self):
    """Closes session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
