import os

import psutil

from dbs.init_mongodb import mongo


class MongoDBConnectionChecker:
    def __init__(self, mongo_connection):
        self.mongo = mongo_connection

    def count_connection(self):
        num_connection = self.mongo.active_connections()  # TODO: [Section 3] Find the way to get number of Mongodb connections
        print('Number of connections:', num_connection)

        return num_connection

    def check_overload(self):
        # num_connection = self.mongo.active_connections()  # TODO: [Section 3] Find the way to get number of Mongodb connections
        num_connection = 100
        num_core = os.cpu_count()
        process = psutil.Process()
        memory_usage = process.memory_info().rss
        max_connection = num_core * 1000  # TODO: [Section 3] Find suitable number of connections per core

        print('Number of connections:', num_connection)
        print(f'Memory usage: {memory_usage / 1024 / 1024} MB')

        offset = 100
        if num_connection > max_connection - offset:
            print(f'Overload warning: {num_connection}/{max_connection}')
            # We can send a mail to notify here


overload_checker = MongoDBConnectionChecker(mongo)
