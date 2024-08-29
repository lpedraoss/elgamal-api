# login.py
from flask import Blueprint, request, jsonify, render_template
from database import get_db_connection
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
    
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    # Verificar si la tabla 'users' existe y crearla si no existe
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL UNIQUE,
        password TEXT NOT NULL,
        p VARCHAR(255) NOT NULL,
        a VARCHAR(255) NOT NULL,
        c1 VARCHAR(255) NOT NULL
    )
    """)
    
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    
    cursor.close()
    connection.close()
    
    if user and verify_password(password, eval(user['password']), int(user['p']), int(user['a']), int(user['c1'])):
        return jsonify({'message': 'Login successful!'}), 200
    else:
        return jsonify({'message': 'Login failed. Check your username and/or password.'}), 401