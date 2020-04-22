from main.models import db, User, Date
from sqlalchemy.orm import joinedload
import time
import datetime
import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

def slow():
    git = {}
    dates = db.session.query(Date).all()
    for date in dates:
        print(date.day, date.users)
        #git[str(date.day)] = len(date)

def fast():
    git = {}
    today = datetime.datetime(2020, 4, 21)
    dates = db.session.query(Date).options(joinedload('users')).all()
    for date in dates:
        print(date.users)
        git[str(date.day)] = len(date.users)

def git_proken():
    git_data = {}
    proken_data = {}
    dates = db.session.query(Date).all()
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

if __name__ == '__main__':
    start = time.time()
    #data = slow()
    #data = fast()
    data = git_proken()
    elapsed_time = time.time() - start
    print(elapsed_time)
    #print(data)
