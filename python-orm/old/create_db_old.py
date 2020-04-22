from main.models import db, User, Date, Record, init
import datetime
from random import randint, sample

names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

def make_user():
    for i in range(10):
        user = User(name=names[i])
        db.session.add(user)

    db.session.commit()

def make_date():
    d = datetime.datetime(2019, 1, 1)
    while d <= datetime.datetime(2020, 12, 31):
        day = Date(day=d)
        db.session.add(day)
        d += datetime.timedelta(days=1)

    db.session.commit()

def make_time(user_id, date_id, day):
    s = datetime.time(randint(15, 18), 0, 0)
    e = datetime.time(randint(19, 22), 0, 0)
    start = datetime.datetime.combine(day, s)
    end = datetime.datetime.combine(day, e)

    return Record(user_id=user_id, date_id=date_id, start=start, end=end)

def choose_users():
    return sample(names, randint(0,10))

def make_record():
    for date in Date.query.all():
        members = 0
        for user in choose_users():
            if user is None:
                continue
            else:
                user_id=User.query.filter_by(name=user).first().id
                data = make_time(user_id, date.id, date.day)
                db.session.add(data)
                members += 1

        date.sum = members
        db.session.add(date)
        db.session.commit()

if __name__ == '__main__':
    init()
    make_user()
    make_date()
    make_record()
