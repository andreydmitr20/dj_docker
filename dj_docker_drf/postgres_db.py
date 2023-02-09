from array import array
import psycopg2


class Postgres_db:
    def __init__(self, dbname, username, password):
        self.__dbname = dbname
        self.__username = username
        self.__password = password
        self.__conn = None

    def connect(self):
        try:
            self.__conn = psycopg2.connect(
                f"""
               dbname={self.get_dbname()}
               user={self.get_username()}
               host='postgresql'
               password={self.__password}
               connect_timeout=1
               """)
            self.conn().autocommit = True
        except:
            self.__conn = None
        return self.__conn

    def disconnect(self):
        if self.__conn != None:
            self.__conn.close()

    def get_username(self): return self.__username
    def get_dbname(self): return self.__dbname
    def conn(self): return self.__conn

    def get_json(self,
                 sql: str,
                 id_field: str,
                 fields: list):
        # Setting auto commit false

        cur = self.conn().cursor()
        # Retrieving data
        cur.execute(sql.replace('*', id_field+','+','.join(fields)))
        json = {}
        for tup in cur.fetchall():
            json[tup[0]] = [tup[i] for i in range(1, len(tup))]

        # self.conn().commit()
        # Closing the connection
        # self.conn().close()
        return json

    def is_connected(self): return True if self.conn() != None else False


if __name__ == "__main__":
    d = Postgres_db('postgres',
                    'postgres',
                    'changeme')
    d.connect()
    if (d.is_connected()):
        print(d.get_json(
            '''SELECT * from "user"''',
            ['user_id', 'name', 'api_key']))
