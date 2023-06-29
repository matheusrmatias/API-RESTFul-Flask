from api import ma
from ..models import Client_Model
from marshmallow import fields

class ClientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Client_Model.Client
        load_instance = True
        fields = ('idClient', 'name', 'fone', 'maritalStatus', 'address')

    name = fields.String(required=True)
    fone = fields.String(required=True)
    maritalStatus = fields.String(required=True)
    address = fields.String(required=True)