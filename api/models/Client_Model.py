from api import db

class Client(db.Model):
    __tablename__ = 'clients'
    idClient = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    fone = db.Column(db.String(11), nullable=False)
    maritalStatus = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(60), nullable=False)