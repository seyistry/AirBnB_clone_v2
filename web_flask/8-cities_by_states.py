#!/usr/bin/python3
"""
List of states
"""
from models import storage
from models.state import State

from flask import Flask, render_template, abort

app = Flask(__name__)
app.url_map.strict_slashes = False
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route('/cities_by_states')
def run_all_states_cites():
    """Run all states"""
    l_list = storage.all(State)
    return render_template('8-cities_by_states.html', l_list=l_list)


@app.teardown_appcontext
def do_teardown(self):
    """Closes session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
