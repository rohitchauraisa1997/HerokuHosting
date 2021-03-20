import sqlite3
from db import db

# This Model is an API, this API exposes two endpoints
# find_by_username and find_by_id method
# these two endpoints are used in security.py(REST API)
# the REST Api doesnt care in what way these endpoints 
# are written as long as these apis return back the same data.
class UserModel(db.Model):
    """
    This User class is not a resource because api 
    doesnt rx data or send this class as a json presentation.
    This is like a helper class.
    """
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.String(80))
    password = db.Column("password", db.String(80))
        
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        print("@"*30)
        print(username)
        print(cls.query.filter_by(username=username))
        print("@"*30)
        return cls.query.filter_by(username=username).first()
    
    @classmethod
    def find_by_id(cls, _id):
        print(id)
        print(cls.query.filter_by(id=_id))
        return cls.query.filter_by(id=_id).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()