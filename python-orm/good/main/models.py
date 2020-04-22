from main import db

class Record(db.Model):
    __tablename__ = "records"

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    date_id = db.Column(db.Integer, db.ForeignKey('dates.id'), primary_key=True)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)

    user = db.relationship('User')
    date = db.relationship('Date')

    def __repr__(self):
        return '<user_id={self.user_id} date_id={self.date_id} start={self.start} end={self.end}>'.format(self=self)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    active = db.Column(db.Boolean, nullable=False, default=False)
    dates = db.relationship(
            'Date',
            secondary=Record.__tablename__,
            back_populates='users',
                            )
    user_date = db.relationship('Record')

    @classmethod
    def authenticate(cls, query, name):
        user = query(cls).filter(cls.name==name).first()
        return user

    def __repr__(self):
        return '<User id={self.id} name={self.name!r} active={self.active}>'.format(self=self)

class Date(db.Model):
    __tablename__ = "dates"

    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.DateTime, nullable=False)
    sum = db.Column(db.Integer, default=0, nullable=False)

    users = db.relationship(
            "User",
            secondary=Record.__tablename__,
            back_populates='dates',
        )

    user_date = db.relationship('Record')

    def __repr__(self):
        return '<Id={self.id} day={self.day} members={self.sum}>'.format(self=self)

def init():
    db.create_all()
