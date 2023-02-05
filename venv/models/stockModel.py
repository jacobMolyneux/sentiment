from app import db

class Stocks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ticker = db.Column(db.String)

    
