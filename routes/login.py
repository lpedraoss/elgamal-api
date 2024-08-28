from flask import Blueprint, request, jsonify, render_template
from database import users_db
from utils.encryption import verify_password

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@login_blueprint.route('/login', methods=['POST'])
def login():
    if request.is_json:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
    
    user = next((user for user in users_db if user['username'] == username), None)
    
    if user and verify_password(password, user['password'], user['p'], user['a'], user['c1']):
        return jsonify({'message': 'Login successful!'}), 200
    else:
        return jsonify({'message': 'Login failed. Check your username and/or password.'}), 401