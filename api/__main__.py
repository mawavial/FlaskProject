from flask import (Flask, jsonify, request)
from api.views import (driver_api, truck_api)
from repository.content_manager import ContentManager

app = Flask(__name__)

API_NAME = "/api/v1"

app.add_url_rule("/drivers", view_func=driver_api.list_drivers, methods=["GET"])
app.add_url_rule("/drivers", view_func=driver_api.get_driver_by_id, methods=["GET"])
app.add_url_rule("/drivers", view_func=driver_api.save_driver, methods=["POST"])
app.add_url_rule("/drivers", view_func=driver_api.delete_driver, methods=["DELETE"])


app.add_url_rule("/trucks", view_func=driver_api.list_trucks, methods=["GET"])
app.add_url_rule("/trucks", view_func=driver_api.get_truck_by_id, methods=["GET"])
app.add_url_rule("/trucks", view_func=driver_api.save_truck, methods=["POST"])
app.add_url_rule("/trucks", view_func=driver_api.delete_truck, methods=["DELETE"])

if __name__ == "__main__":
    connector = ContentManager()
    app.run(host="0.0.0.0", debug=True, use_reloader=True)