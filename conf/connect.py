import os
from conf import config
from pymongo import MongoClient


class Connect:

    def connections(self):
        if os.environ['ENV'] == 'dev':
            cnf = config.DevelopmentConfig
        else:
            cnf = config.ProductionConfig
        my_client = MongoClient(host=cnf.DB_HOST, port=cnf.PORT)
        db = my_client.LostArk
        return db

