from flask import request, redirect, url_for, render_template, flash, session, jsonify
from main import app, db
from main.models import db, User, Date
from sqlalchemy.orm import joinedload
import time
import datetime
import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

def git_proken():
    git_data = {}
    proken_data = {}
    dates = db.session.query(Date).\
            options(joinedload('users')).all()
    target_day = dates[0].day
    git_data[target_day.timestamp()] = 0
    proken_data[target_day] = []
    for date in dates:
        if date.day == target_day:
            git_data[target_day.timestamp()] += 1
        else:
            target_day = date.day
            git_data[target_day.timestamp()] = 1
            proken_data[target_day] = []

        proken_data[target_day].append(date.users.name)

    return git_data

@app.route('/')
def index():
    data = git_proken()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    start = time.time()
    data = git_proken()
    elapsed_time = time.time() - start
    print(elapsed_time)
    #print(data)
