from repository.content_manager import ContentManager
from repository.db_connector_redis import DBConnectorRedis
from utils.constants import UIID

CLIENT_ID = f"{UIID}-client"


class ClientManager(ContentManager):
    def __init__(self, connector=None):
        self.connector = connector if connector else DBConnectorRedis()
        pass

    def save_document(self, client):
        try:
            id = f"{CLIENT_ID}"
            client_json = client.to_dict()
            self.connector.save(id, client_json)
        except Exception as e:
            print(e)

    def get_document(self, client_id):
        id = f"{CLIENT_ID}"
        client = self.connector.get_by_id(id, client_id)
        return client.to_dict()

    def get_all_documents(self):
        clients = self.connector.get_all()
        return clients

    def delete(self, client_id):
        id = f"{CLIENT_ID}"
        self.connector.delete(id, client_id)
        pass