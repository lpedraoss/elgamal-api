from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv('DB2_HOST'),
        user=os.getenv('DB2_USER'),
        password=os.getenv('DB2_PASSWORD'),
        database=os.getenv('DB2_NAME'),
        port=int(os.getenv('DB1_PORT'))  # Asegúrate de convertir el puerto a un entero
    )
    return connection