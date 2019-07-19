from openDoor import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    password = db.Column(db.String(128), index = True)

    def __repr__(self):
        return '<User: %r>' % (self.username)


class Session(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    session = db.Column(db.String(128), index = True, unique = True)
    data = db.Column(db.String(128))
    expire = db.Column(db.Integer)

    def __repr__(self):
        return '<SessionId: %r>' % (self.sessionid)