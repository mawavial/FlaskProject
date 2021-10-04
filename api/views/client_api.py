import json
from flask import request, jsonify
from repository.client_manager import  ClientManager
from models.client_model import Client

import app

CLIENT_TYPE = "client"


def save_client():
    a = request.json
    keys = ["ci", "age", "name", "email", "cellphone", "address", "nit"]
    for k in keys:
        if k not in a:
            raise jsonify({"message": f"{k} parameters are required"})
    client_obj = Client(a["ci"], a["age"], a["name"], a["email"], a["cellphone"], a["address"], a["nit"])
    connector = ClientManager()
    connector.save_document(client_obj.__dict__)
    return jsonify({"message": "the client was saved successfully"})


def get_client_by_id(client_id):
    connector = ClientManager()
    result = connector.get_document(client_id)
    if result:
        return jsonify(json.loads(result))
    else:
        return jsonify({"message": "Not found"}), 404


def list_clients():
    connector = ClientManager()
    print(connector)
    result = connector.get_all_documents()
    print(result)
    if result:
        return jsonify(json.loads(result))
    else:
        return jsonify({"message": "Not found"}), 404


def delete_client_by_id(client_id):
    connector = ClientManager()
    connector.delete(client_id, CLIENT_TYPE)
    return jsonify({"message": "client was deleted successfully"})