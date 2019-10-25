from flask import request, redirect, url_for, render_template, flash
from flaskr import app, db

@app.route('/')
def index():
    name = "syukwsk"
    return render_template('index.html', name=name)

