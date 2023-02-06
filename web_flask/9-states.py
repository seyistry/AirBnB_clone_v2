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


@app.route('/states')
def run_all_states():
    """Run all states"""
    l_list = storage.all(State)
    return render_template('7-states_list.html', l_list=l_list)


@app.route('/states/<id>')
def run_all_states_cites(id):
    """Run all states"""
    states = storage.all(State)
    state_id = 'State.' + id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def do_teardown(self):
    """Closes session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
