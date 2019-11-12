from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from random import randint

# DB接続
engine = create_engine('sqlite:///flaskr.db')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    dates = relationship("Date", backref="users")
 
    def __repr__(self):
        return '<User id={id} name={name}>'.format(id=self.id, name=self.name)
class Date(Base):
    __tablename__ = 'dates'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    day = Column(String)
    start = Column(String)
    end = Column(String)
    user = relationship("User")

# テーブルクラスのテーブルを生成
Base.metadata.create_all(engine)
 
# セッション生成
Session = sessionmaker(bind=engine)
session = Session()

session.add(User(name="A"))
session.add(User(name="B"))
session.add(User(name="C"))
session.add(User(name="D"))
session.add(User(name="E"))
session.add(User(name="F"))
session.add(User(name="G"))
session.add(User(name="H"))
session.add(User(name="I"))
session.add(User(name="J"))

session.commit()

users = session.query(User).all()

print(users)

def random_user():
    return randint(1, 10)

def random_day():
    random_month = randint(1, 12)
    random_day = randint(1, 31)
    return str(random_month)+"/"+str(random_day)

def random_time(time):
    if time == "start":
        random_start = randint(8, 15)
        return str(random_start)+":00"

    elif time == "end":
        random_end = randint(16, 22)
        return str(random_end)+":00"


for i in range(10):
    user = random_user()
    day = random_day()
    start = random_time("start")
    end = random_time("end")
    session.add(Date(users_id=user, day=day, start=start, end=end))
    print(user, day, start, end)

session.commit()
print("save")
users = session.query(User).join(Date, User.id == Date.users_id).all()
 
for user in users:
    print("%sさんの出席" % (user.name))
    for date in user.dates:
        print("|- 日付：%s 出：%s 帰：%s" % (date.day, date.start, date.end))
   
    print('')
