from abc import ABCMeta, abstractmethod


class Person(metaclass=ABCMeta):
    """Class to define basic information of a person"""

    def __init__(self, ci, age, name, email, cellphone, address):
        self.ci = ci
        self.age = age
        self.name = name
        self.email = email
        self.cellphone = cellphone
        self.address = address

    @abstractmethod
    def to_dict(self):
        """
        something --> This method need to be implemented
        Arg:
        """
        pass
