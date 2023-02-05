#!/usr/bin/python3
"""
a script that starts a Flask web
application. C is fun!
"""


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def print_hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def print_hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def print_c_fun(text):
    value = text.replace("_", " ")
    return "C %s" % value


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
