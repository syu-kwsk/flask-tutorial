from flaskr import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    dates = db.relationship("Date", lazy="select", backref=db.backref("user", lazy='joined'))

    def __repr__(self):
        return '<User id={id} name={name}>'.format(id=self.id, name=self.name)

class Date(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    day = db.Column(db.Text)
    start = db.Column(db.Text)
    end = db.Column(db.Text)


    def __repr__(self):
        return '<Date id={id} day={day} start={start} end={end}>'.format(
                id=self.id, day=self.day, start=self.start, end=self.end)

def init():
    db.create_all()
