from flask_restful import Resource
from api import api
from flask import request, make_response, jsonify
from ..entitys import Client
from ..schemas import Client_Schema
from ..services import Client_Service


class ClientList(Resource):
    def get(self):
        clients = Client_Service.list_client()
        cs = Client_Schema.ClientSchema(many=True)
        return make_response(cs.jsonify(clients), 200)

    def post(self):
        cs = Client_Schema.ClientSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json['name']
            fone = request.json['fone']
            maritalStatus = request.json['maritalStatus']
            address = request.json['address']

            new_client = Client.Client(name=name, fone=fone, maritalStatus=maritalStatus, address=address)
            result = Client_Service.registes_client(new_client)
            return make_response(cs.jsonify(result), 200)
class ClientDetail(Resource):

    def get(self, idClient):
        client = Client_Service.list_client_id(idClient)
        if client is None:
            return make_response(jsonify("Client not found"), 404)
        cs = Client_Schema.ClientSchema()
        return make_response(cs.jsonify(client), 200)

    def put(self, idClient):
        client_db = Client_Service.list_client_id(idClient)
        if client_db is None:
            return make_response(jsonify("Client not found"), 404)
        cs = Client_Schema.ClientSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json['name']
            fone = request.json['fone']
            maritalStatus = request.json['maritalStatus']
            address = request.json['address']
            new_client = Client.Client(name=name, fone=fone, maritalStatus=maritalStatus, address=address)
            Client_Service.update_client(client_db, new_client)
            current_client = Client_Service.list_client_id(idClient)
            return make_response(cs.jsonify(current_client), 200)

    def delete(self, idClient):
        client_db = Client_Service.list_client_id(idClient)
        if client_db is None:
            return make_response(jsonify("Client not found"), 404)
        Client_Service.remove_client(client_db)
        return make_response('Client removed', 200)

api.add_resource(ClientList, '/clients')
api.add_resource(ClientDetail, '/clients/<int:idClient>')