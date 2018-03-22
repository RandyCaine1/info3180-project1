from . import db


class UserProfile(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    email = db.Column(db.String(80))
    gender = db.Column(db.String(10))
    location = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    photo = db.Column(db.String(80))
    created_on = db.Column(db.String(20))
    

    def __init__(self,firstname,lastname,gender,email,location,bio,created_on,photo):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.email = email
        self.location = location
        self.bio = bio
        self.created_on = created_on
        self.photo = photo
    
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
