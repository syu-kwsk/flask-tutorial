from main.models import db, User, Date, Record, init
import datetime
from random import randint, sample
from tqdm import tqdm
names = ['わたる', 'タケシ', 'ハナコ', 'タロウ', 'シュンペイ', 'コナン', 'シンイチ', 'コウタ', 'サトシ', 'ヨシコ']

def make_user():
    for i in range(10):
        user = User(name=names[i])
        db.session.add(user)

    db.session.commit()

def make_date():
    d = datetime.datetime(2020, 4, 1)
    while d <= datetime.datetime(2030, 4, 1):
        day = Date(day=d)
        db.session.add(day)
        d += datetime.timedelta(days=1)

    db.session.commit()

def make_time(day):
    s = datetime.time(randint(15, 18), 0, 0)
    e = datetime.time(randint(19, 22), 0, 0)
    start = datetime.datetime.combine(day, s)
    end = datetime.datetime.combine(day, e)

    return [start, end]

def choose_users():
    return sample(names, randint(0,10))

def make_record():
    data = []
    for date in tqdm(Date.query.all()):
        data = []
        #members = 0
        users = []
        for user in choose_users():
            if user is None:
                continue
            else:
                user=User.query.filter_by(name=user).first()
                time = make_time(date.day)
                record = Record(start=time[0], end=time[0], user=user, date=date)
                users.append(record)
                data.append(record)
                #members += 1
        date.user_date = users
        data.append(date)

    db.session.add_all(data)
    db.session.commit()

if __name__ == '__main__':
    init()
    make_user()
    make_date()
    make_record()
