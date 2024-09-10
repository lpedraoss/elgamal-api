from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

load_dotenv()

db = SQLAlchemy()

# Cargar las variables de entorno
DB_USER = os.getenv('DB2_USER')
DB_PASSWORD = os.getenv('DB2_PASSWORD')
DB_HOST = os.getenv('DB2_HOST')
DB_NAME = os.getenv('DB2_NAME')
DB_PORT = os.getenv('DB1_PORT')

def connect_to_database(app):
    # Asignar explícitamente las variables de entorno al URI de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)