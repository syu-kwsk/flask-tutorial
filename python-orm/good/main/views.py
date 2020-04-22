from flask import request, redirect, url_for, render_template, flash, session, jsonify
from main import app, db
from main.models import db, User, Date, Record
import time
import datetime
from sqlalchemy.orm import joinedload, lazyload
import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

def git_proken():
    git_data = {}
    proken_data = {}
    dates = db.session.query(Date).options(joinedload('users')).all()
    target_day = dates[0].day
    proken_data[target_day] = []
    for date in dates:
        target_day = date.day
        git_data[target_day.timestamp()] = len(date.users)
        users = []
        for user in date.users:
            users.append(user.name)
        proken_data[target_day] = users

    return [git_data, proken_data]

def git_proken_slow():
    git_data = {}
    proken_data = {}
    dates = db.session.query(Date).all()
    target_day = dates[0].day
    proken_data[target_day] = []
    for date in dates:
        target_day = date.day
        git_data[target_day.timestamp()] = len(date.users)
        users = []
        for user in date.users:
            users.append(user.name)
        proken_data[target_day] = users

    return [git_data, proken_data]

@app.route('/')
def index():
    data = git_proken()
    return render_template('index.html', data=data)

@app.route('/fast')
def fast():
    datas = git_proken()
    return render_template('data.html', git_data=datas[0], proken_data=datas[1])

@app.route('/slow')
def slow():
    datas = git_proken_slow()
    return render_template('data.html', git_data=datas[0], proken_data=datas[1])


if __name__ == '__main__':
    start = time.time()
    data = git_proken()
    elapsed_time = time.time() - start
    print(elapsed_time)
