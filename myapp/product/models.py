from myapp import db

class Product(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255),nullable = False)
    price = db.Column(db.Float(asdecimal=True),nullable = False)
    
    def __init__(self,name,price):
        self.name = name
        self.price = price
        
    def __repr__(self):
        return '<Product %d>' % self.id