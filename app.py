from flask import (Flask, jsonify, request)
from api.views import (driver_fake_api, truck_fake_api, client_api)

app = Flask(__name__)

API_NAME = "/api/v1"

app.add_url_rule("/drivers", view_func=driver_fake_api.list_drivers, methods=["GET"])
app.add_url_rule("/drivers", view_func=driver_fake_api.get_driver_by_id, methods=["GET"])
app.add_url_rule("/drivers", view_func=driver_fake_api.save_driver, methods=["POST"])
app.add_url_rule("/drivers", view_func=driver_fake_api.delete_driver, methods=["DELETE"])


app.add_url_rule("/trucks", view_func=truck_fake_api.list_trucks, methods=["GET"])
app.add_url_rule("/trucks/<truck_id>", view_func=truck_fake_api.get_truck_by_id, methods=["GET"])
app.add_url_rule("/trucks", view_func=truck_fake_api.save_truck, methods=["POST"])
app.add_url_rule("/trucks/<truck_id>", view_func=truck_fake_api.delete_truck, methods=["DELETE"])

app.add_url_rule("/clients", view_func=client_api.list_clients, methods=["GET"])
app.add_url_rule("/clients", view_func=client_api.save_client, methods=["POST"])
app.add_url_rule("/clients/<client_id>", view_func=client_api.get_client_by_id)
app.add_url_rule("/clients/<client_id>", view_func=client_api.delete_client_by_id, methods=["DELETE"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6379, debug=True, use_reloader=True)
