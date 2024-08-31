from flask import Flask
from routes.register import register_blueprint
from routes.login import login_blueprint
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.register_blueprint(register_blueprint, url_prefix='/api')
app.register_blueprint(login_blueprint, url_prefix='/api')
#index 
@app.route('/')
def home():
    return "Welcome to the Simple API!"

if __name__ == '__main__':
    app.run(debug=True)