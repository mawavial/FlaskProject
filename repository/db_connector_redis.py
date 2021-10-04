import json
import redis
from redis import TimeoutError, ConnectionError

from repository.db_connector import DBConnector


class DBConnectorRedis(DBConnector):
    def __init__(self):
        self.connection = self.get_connection()

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        # close database connection
        pass

    def get_connection(self):
        try:
            if hasattr(self, 'connection') and self.connection:
                return self.connection
            else:
                self.connection = redis.Redis(host="localhost",
                                              port=6379)
        except (TimeoutError, ConnectionError) as timeout_e:
            print(timeout_e)
            raise Exception("The DB is not available",
                            custom_param="string")
        else:
            return self.connection
        finally:
            print("END OF DB OPERATION")

    def save(self, id_save, object_to_save):
        encode_data = json.dumps(object_to_save)
        result_save = self.connection.set(id_save, encode_data)
        return result_save

    def get_by_id(self, id):
        result_get = self.connection.get(id)
        decode_data = json.loads(result_get)
        return decode_data

    def get_all(self):
        list_objs = []
        list_ids = [id for id in self.connection.scan_iter(count=20)]
        if len(list_ids) > 0:
            list_objs = self.connection.mget(list_ids)
            list_objs = [json.loads(obj) for obj in list_objs]
        return list_objs

    def get_by_pattern(self, pattern):
        pattern = f"{pattern}*"
        list_objs = []
        list_ids = [id for id
                    in self.connection.scan_iter(match=pattern,
                                                 count=20)
                    ]
        if len(list_ids) > 0:
            list_objs = self.connection.mget(list_ids)
            list_objs = [json.loads(obj) for obj in list_objs]
        return list_objs

    def delete(self, id):
        result_get = self.connection.get(id)
        self.connection.delete(result_get.keys())
