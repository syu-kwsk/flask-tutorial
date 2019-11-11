from flaskr import db

class Date(db.Model):
    __tablename__ = 'days'
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Text)

    def __repr__(self):
        return '<Date id={id} day={day}>'.format(
                id=self.id, day=self.day)

def init():
    db.create_all()
