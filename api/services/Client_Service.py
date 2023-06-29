from ..models import Client_Model
from api import db

def registes_client(client):
    client_db = Client_Model.Client(
        name = client.name,
        fone = client.fone,
        maritalStatus = client.maritalStatus,
        address = client.address
    )
    db.session.add(client_db)
    db.session.commit()
    return client_db

def list_client():
    clients = Client_Model.Client.query.all()
    return clients

def list_client_id(idClient):
    client = Client_Model.Client.query.filter_by(idClient=idClient).first()
    return client

def update_client(old_client, new_client):
    old_client.name = new_client.name
    old_client.fone = new_client.fone
    old_client.maritalStatus = new_client.maritalStatus
    old_client.address = new_client.address
    db.session.commit()

def remove_client(client):
    db.session.delete(client)
    db.session.commit()