from flask import request, redirect, url_for, render_template, flash
from flaskr import app, db

@app.route('/')
def index():
    name = "syukwsk"
    return render_template('index.html', name=name)

@app.route('/attend/<string:name>')
def attend(name):
    print("/attend")
    name = name + " attended"
    return render_template('index.html', name=name)
