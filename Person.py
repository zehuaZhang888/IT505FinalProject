import sqlite3


class Person:
    def __init__(self, db):
        self.db = db
        self.create_table()

    def create_table(self):
        query = "CREATE TABLE IF NOT EXISTS people (name TEXT NOT NULL,\
         phone_number INTEGER NOT NULL, email_address TEXT NOT NULL );"
        self.db.execute_query(query)

    def add_person(self, name, phone, email):
        query = "INSERT INTO people (name, phone_number, email_address) VALUES (?, ?, ?)"
        params = (name, phone, email)
        self.db.execute_query(query, params)