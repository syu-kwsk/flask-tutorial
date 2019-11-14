from flask import request, redirect, url_for, render_template, flash
from flaskr import app, db
from flaskr.models import User, Date 
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user = request.form['name']
        user = User.query.filter(User.name == user).first()
        if user is None:
            flash('Invalid User Name')
        else:
            return render_template('home.html', user=user)
    return render_template('index.html')

@app.route('/attend/<string:name>')
def attend(name):
    print("/attend")
    name = name + " attended"
    return render_template('index.html', name=name)
