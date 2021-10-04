from abc import ABCMeta, abstractmethod


class Vehicle(metaclass=ABCMeta):
    """Class to define basic information of a person"""

    def __init__(self, vehicle_id, vehicle_type, name, manufacturer):
        self.vehicle_id = vehicle_id
        self.name = name
        self.vehicle_type = vehicle_type
        self.manufacturer = manufacturer

    @abstractmethod
    def to_dict(self):
        """
        something --> This method need to be implemented
        Arg:
        """
        pass
