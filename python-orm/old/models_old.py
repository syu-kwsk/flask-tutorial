from main import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    active = db.Column(db.Boolean, nullable=False, default=False)
    records = db.relationship('Record',
                            lazy='joined',
                            backref=db.backref('user', lazy='joined')
                            )

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
    records = db.relationship("Record",
                            lazy="joined",
                            backref=db.backref("date", lazy='joined')
                            )
    sum = db.Column(db.Integer, default=0, nullable=False)

    def __repr__(self):
        return '<Id={self.id} day={self.day} members={self.sum}>'.format(self=self)

class Record(db.Model):
    __tablename__ = "records"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date_id = db.Column(db.Integer, db.ForeignKey('dates.id'))
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Id={self.id} user_id={self.user_id} date_id={self.date_id} start={self.start} end={self.end}>'.format(self=self)

def init():
    db.create_all()
