from main import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    active = db.Column(db.Boolean, nullable=False, default=False)
    dates = db.relationship(
            'Date',
            backref='users',
            lazy=True
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
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    day = db.Column(db.DateTime, nullable=False)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Id={self.id} user_id={self.user_id} day={self.day} start={self.start} end={self.end}>'.format(self=self)

def init():
    db.create_all()
