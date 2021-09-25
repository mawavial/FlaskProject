from abc import ABCMeta, abstractmethod
from repository.content_manager import ContentManager

CLIENT_ID = "UUID-client"

class ClientManager(ContentManager):
    def __init__(self):
        pass

    def save_document(self, ci, client):
        pass

    def get_document(self):
        pass

    def get_all(self):
        pass

    def delete(self):
        pass
