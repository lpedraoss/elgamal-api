from database import db

class User(db.Model):
    __tablename__ = 'users'  # Especificar el nombre de la tabla
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    p = db.Column(db.String(255), nullable=False)
    a = db.Column(db.String(255), nullable=False)
    c1 = db.Column(db.String(255), nullable=False)