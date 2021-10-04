from abc import ABCMeta, abstractmethod


class DBConnector(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def get_connection(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def get_by_id(self):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_pattern(self):
        pass

    @abstractmethod
    def delete(self):
        pass