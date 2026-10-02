"""
db.py
------
مسؤول عن حاجة واحدة بس: فتح وقفل الاتصال بقاعدة البيانات.
ده مبدأ Separation of Concerns - الكلاس ده معندوش أي فكرة عن employees
أو managers، هو بس بيعرف يوصّل ويقطع الاتصال.
"""

import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self, host="localhost", user="root", password="", database="company"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """ opens the connection to the database"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return self.connection
        except Error as e:
            raise ConnectionError(f" failed to connect to the database: {e}")

    def close(self):
        """ closes the connection."""
        if self.connection and self.connection.is_connected():
            self.connection.close()

    # __enter__ و __exit__ بيخلوا الكلاس يشتغل مع "with" statement
    # يعني تقدر تكتب: with Database() as db:  ... وهو هيقفل نفسه لوحده
    # حتى لو حصل خطأ جوه الـ with block
    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
