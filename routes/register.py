import random
from math import pow
from flask import Blueprint, request, jsonify
from database import users_db
from utils.encryption import gen_key, power, encrypt

register_blueprint = Blueprint('register', __name__)

@register_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if any(user['username'] == username for user in users_db):
        return jsonify({'message': 'Username already exists.'}), 409
    
    p = random.randint(pow(10, 20), pow(10, 50))
    g = random.randint(2, p)
    a = gen_key(p)
    e = power(g, a, p)
    
    en_password, c1 = encrypt(password, p, e, g)
    
    new_user = {
        'username': username,
        'password': en_password,
        'p': p,
        'a': a,
        'c1': c1
    }
    users_db.append(new_user)
    
    return jsonify({'message': 'User registered successfully!'}), 201