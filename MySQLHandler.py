import mysql.connector
from mysql.connector import Error


class MySQLHandler:
    def __init__(self, host, database, user, password):
        try:
            self.connection = mysql.connector.connect(host=host,
                                                      database=database,
                                                      user=user,
                                                      password=password)
        except Error as e:
            print("Error while connecting to MySQL", e)

    def show_tables(self):
        cursor = self.connection.cursor()
        cursor.execute("SHOW TABLES")
        result = cursor.fetchall()

        for x in result:
            print(x)

    def insert(self, sql, val):
        cursor = self.connection.cursor()
        cursor.executemany(sql, val)

        self.connection.commit()
        cursor.close()

    def create_table(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
