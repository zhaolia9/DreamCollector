import os
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("DB_PASSWORD"), # Set your DB password in environment variable DB_PASSWORD
        database="aurelia"
    )
