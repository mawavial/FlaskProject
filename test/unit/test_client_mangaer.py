import pytest
from repository.client_manager import ClientManager
from repository.db_connector import DBConnector
from models.client import Client

@pytest.fixture
def db_connector():
    dbcon = DBConnector()
    return dbcon


def save_document(self, Client):

    pass


def get_document(self):
    pass

def get_all(self):
    pass


def delete(self):
    pass