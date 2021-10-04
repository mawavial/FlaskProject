from abc import ABCMeta, abstractmethod
from models.veichle_model import Vehicle


class Truck(Vehicle):
    """Class to define basic information of a person"""

    def __init__(self, vehicle_id, truck_id, vehicle_type, name, manufacturer, license_plate, model):
        super(Truck, self).__init__(vehicle_type, truck_id, name, manufacturer)
        self.truck_id = truck_id
        self.license_plate = license_plate
        self.model = model

    def to_dict(self):
        dict_init = self.__dict__
        return dict_init
