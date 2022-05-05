import sqlite3
from sqlite3 import Error


class DataBaseEngine:
    def __init__(self, default_file="DB/BusiDiscordUsers.db"):
        self.default_file = default_file

    def build_db(self, db_file=None):
        if not db_file:
            db_file = self.default_file
        connection = self.create_connection(db_file)
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS USERS")
        table = """CREATE TABLE USERS (
        uname VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL
        );"""
        cursor.execute(table)

    def insert_users_data(self, db_file=None):
        if not db_file:
            db_file = self.default_file
        connection = self.create_connection(db_file)
        cursor = connection.cursor()
        sql = """INSERT INTO USERS(uname, email)
        VALUES("noobmaster", "noobmaster@gmail.com")
        """
        cursor.execute(sql)
        connection.commit()
        return cursor.lastrowid

    def select_all(self, db_file=None, table="USERS"):
        if not db_file:
            db_file = self.default_file
        connection = self.create_connection(db_file)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    def create_connection(self, db_file=None):
        if not db_file:
            db_file = self.default_file
        connection = None
        try:
            connection = sqlite3.connect(db_file)
        except Error as err:
            print(err)
        return connection
