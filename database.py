from dotenv import load_dotenv
import mysql.connector
import os
import sqlite3

def get_db_connection():
    db_path = "data/users.db"
    connection = sqlite3.connect(db_path)
    return connection

