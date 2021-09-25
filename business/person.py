from abc import ABCMeta, abstractmethod

class Person(metaclass=ABCMeta):
    """Class to define basic information of a person"""

    def __init__(self, name, last_name, cellphone, email, address, ci=None):
        self.name = name
        self.last_name = last_name
        self.cellphone = cellphone
        self.email = email
        self.address = address
        self.ci = ci

    @abstractmethod
    def _to_dict(self):
        """ something --> this method needs to be implemented """
        pass

