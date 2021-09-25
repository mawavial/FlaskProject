from abc import ABCMeta, abstractmethod


class ContentManager(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def save_document(self):
        pass

    @abstractmethod
    def get_document(self):
        pass

    @abstractmethod
    def delete_document(self):
        pass

    @abstractmethod
    def update_document(self):
        pass
