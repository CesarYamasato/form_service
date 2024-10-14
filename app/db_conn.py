import psycopg2

class DbConnection:

    def __init__(self, db_name, address, port,credentials):
        self.__db_conn = psycopg2.connect(database = db_name, host = address, port = port, user = credentials['user'], password = credentials['password'])