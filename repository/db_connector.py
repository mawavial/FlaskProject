import redis
import json

class DBConnector:
    def __init__(self):
        self.connection = None
        self.connection = self.get_connection()

    def __enter__(self):
        print('Starting')
        return self.connection

    # not necessary for redis
    def __exit__(self, *exc):
        # print('Finishing')
        # self.connection.close()
        pass



    def get_connection(self):
        try:
            if hasattr(self, 'connection') and self.connection:
                return self.connection
            else:
                self.connection = redis.Redis(host="localhost",
                                              port=6379)
        except (TimeoutError, ConnectionError) as timeout_e:
            raise Exception("The DB is not available",
                            custom_param="string")
        else:
            return self.connection
        finally:
            print("finally")

    def save(self, id_save, object_to_save):
        encoded_data = json.dumps(object_to_save)
        result_save = self.connection.set(id_save, encoded_data)
        return result_save

    def get_by_id(self, id_save):
        result_get = self.connection.get(id_save)
        decoded_data = json.loads(result_get)
        return decoded_data

    def get_all(self, pattern):
        pattern = f"{pattern}*"
        list_objs = []
        list_ids = [id for id in self.connection.scan_iter(match=pattern,
                                                           count=20)]
        if(len(list_ids)) > 0:
            list_objs = self.connection.mget(list_ids)
            list_objs = [json.loads(obj) for obj in list_objs]
            return list_objs
