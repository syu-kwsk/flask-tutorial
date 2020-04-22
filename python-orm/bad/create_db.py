from main.models import db, User, init, Date
import datetime
from random import randint, sample

names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

def make_user():
    for i in range(10):
        user = User(name=names[i])
        db.session.add(user)

    db.session.commit()

def choose_users():
    return sample(names, randint(0,10))

def make_record():
    d = datetime.datetime(2020, 4, 1)
    data = []
    while d < datetime.datetime(2120, 4, 1):
        for user in choose_users():
            if user is None:
                continue
            else:
                user_id = User.query.filter_by(name=user).first().id
                s = datetime.time(randint(15, 18), 0, 0)
                e = datetime.time(randint(19, 22), 0, 0)
                start = datetime.datetime.combine(d, s)
                end = datetime.datetime.combine(d, e)
                date = Date(user_id=user_id, day=d, start=start, end=end)
                data.append(date)
        d += datetime.timedelta(days=1)

    db.session.add_all(data)
    db.session.commit()

if __name__ == '__main__':
    init()
    make_user()
    make_record()
