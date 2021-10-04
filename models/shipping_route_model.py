from models.client_model import Client
from models.truck_model import Truck
from models.driver_model import Driver


class ShippingRoute(Truck, Driver, Client):
    """Describes a shipping route """
    def __init__(self, vehicle_id, truck_id, client_id, driver_id, start_place, end_place, packages, status):
        super(Truck, Driver, Client).__init__(self, vehicle_id, client_id, truck_id, driver_id, start_place, end_place, packages, status)
        self.start_place = start_place
        self.end_place = end_place
        self.status = status

    def to_dict(self):
        dict_init = self.__dict__
        return dict_init