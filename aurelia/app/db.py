import os
import mysql.connector

def get_connection():
    password = os.getenv("AURELIA_DB_PASSWORD")# Make sure to set the DB_PASSWORD environment variable before running the application

    if not password:
        raise ValueError("Set AURELIA_DB_PASSWORD environment variable")

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
        database="aurelia"
    )