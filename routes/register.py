import random
from math import pow
from flask import Blueprint, request, jsonify, render_template
from models.models import db, User
from utils.encryption import gen_key, power, encrypt

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
    
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists.'}), 409
    
    p = random.randint(pow(10, 20), pow(10, 50))
    g = random.randint(2, p)
    a = gen_key(p)
    e = power(g, a, p)
    
    en_password, c1 = encrypt(password, p, e, g)
    
    new_user = User(username=username, password=en_password, p=str(p), a=str(a), c1=str(c1))
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully!'}), 201
