from db import db

class StoreModel(db.Model):
    """
    This User class is not a resource because api 
    doesnt rx data or send this class as a json presentation.
    This is like a helper class.
    """
    __tablename__= "stores"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    items = db.relationship('ItemModel',lazy = "dynamic") 
    
    def __init__(self, name):
        self.name = name

    def json(self):
        # return {"name": self.name, "items": [item.json() for item in self.items]}
        # lazy = dynamic
        
        return {"name": self.name, "items": [item.json() for item in self.items.all()]}
    
    @classmethod
    def find_by_name(cls,name):
        # query is like a querybuilder 
        # we can cascade using filter_by
        print(name)
        print(cls)
        print(cls.query.filter_by(name=name))
        return cls.query.filter_by(name=name).first() #SELECT * FROM __tablename__ WHERE name = name
        
    def save_to_db(self):
        print("~"*50)
        print(self)
        print("~"*50)
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
