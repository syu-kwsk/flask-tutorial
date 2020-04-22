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
        '''users = []
        for user in date.users:
            users.append(user.name)
        proken_data[target_day] = users'''

    return git_data

def git_proken_slow():
    git_data = {}
    proken_data = {}
    dates = db.session.query(Date).all()
    target_day = dates[0].day
    proken_data[target_day] = []
    for date in dates:
        target_day = date.day
        git_data[target_day.timestamp()] = len(date.users)
        '''users = []
        for user in date.users:
            users.append(user.name)
        proken_data[target_day] = users'''

    return git_data

if __name__ == '__main__':
    start = time.time()
    #data = slow()
    #data = fast()
    data = git_proken()
    elapsed_time = time.time() - start
    print(elapsed_time)
