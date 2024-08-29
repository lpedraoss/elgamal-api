from flask import Flask
from models.models import db,User
from routes.register import register_blueprint
from routes.login import login_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()
    
app.register_blueprint(register_blueprint, url_prefix='/api')
app.register_blueprint(login_blueprint, url_prefix='/api')

@app.route('/')
def home():
    return "Welcome to the Simple API!"

if __name__ == '__main__':
    app.run(debug=True)