# register.py
from flask import Blueprint, request, jsonify, render_template
from database import get_db_connection
from utils.encryption import gen_key, power, encrypt
import random
from math import pow

register_blueprint = Blueprint('register', __name__)

@register_blueprint.route('/register', methods=['GET'])
def register_page():
    return render_template('register.html')

@register_blueprint.route('/register', methods=['POST'])
def register():
    if request.is_json:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
    
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    
    if user:
        return jsonify({'message': 'Username already exists.'}), 409
    
    p = str(random.randint(pow(10, 20), pow(10, 50)))
    g = random.randint(2, int(p))
    a = str(gen_key(int(p)))
    e = power(g, int(a), int(p))
    
    en_password, c1 = encrypt(password, int(p), e, g)
    
    cursor.execute(
        "INSERT INTO users (username, password, p, a, c1) VALUES (%s, %s, %s, %s, %s)",
        (username, str(en_password), p, a, str(c1))
    )
    connection.commit()
    cursor.close()
    connection.close()
    
    return jsonify({'message': 'User registered successfully!'}), 201