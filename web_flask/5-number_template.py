#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask, render_template


app = Flask(__name__)
# determine root path of the application


@app.route('/', strict_slashes=False)
def hello_route():
    return "Hello HBNB!"
# define route


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
