import json
from db_config import get_redis_connection
from flask import app

class RetrieveFromRedis:
    @staticmethod
    def retrieve_all_redis_data(key):
        """Retrieve all data stored under a key in Redis.

        Args:
            key (str): The key under which data is stored in Redis.

        Returns:
            dict: The data stored under the key as a dictionary.
        """
        r = get_redis_connection()
        data = r.execute_command('JSON.GET', key)
        if data:
            return json.loads(data)
        else:
            return None
     
    @staticmethod    
    def clear_redis_json(key):
        get_redis_connection().delete(key)
        return f'Cleared Redis JSON key: {key}'


