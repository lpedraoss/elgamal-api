from flask import Flask, redirect, render_template, url_for
from routes.register import register_blueprint
from routes.login import login_blueprint
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', os.urandom(24))  
app.register_blueprint(register_blueprint, url_prefix='/api')
app.register_blueprint(login_blueprint, url_prefix='/api')

# Index route that redirects to login
@app.route('/')
def index():
    return redirect(url_for('login.login_page'))
@app.route('/home')
def home_page():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
