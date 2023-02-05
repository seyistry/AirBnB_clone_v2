#!/usr/bin/python3
"""
a script that starts a Flask web
application. Is it a number!
"""


from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def print_hello():
    return "Hello HBNB!"


@app.route("/hbnb")
def print_hbnb():
    return "HBNB"


@app.route("/c/<text>")
def print_c_fun(text):
    value = text.replace("_", " ")
    return "C %s" % value


@app.route('/python')
@app.route("/python/<text>")
def print_python_fun(text='is cool'):
    value = text.replace("_", " ")
    return "Python %s" % value


@app.route("/number/<int:n>")
def print_check_num(n):
    if isinstance(n, int):
        return "%d is a number" % n


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
