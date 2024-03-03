from db_config import get_redis_connection

class InsertToRedis:
    @staticmethod
    def insertJsonToRedis(key, json_data):
        """Insert JSON data into Redis using the JSON module.

        Args:
            key (str): The key under which to store the JSON data.
            json_data (dict): The JSON data to store.
        """
        r = get_redis_connection()
        r.json().set(key, '.', json_data)
        return True