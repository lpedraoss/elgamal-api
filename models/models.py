from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    p = db.Column(db.String(256), nullable=False)
    a = db.Column(db.String(256), nullable=False)
    c1 = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
