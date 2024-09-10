from flask import Blueprint, request, render_template, redirect, url_for, flash
from models.user import User  # Importar el modelo de usuario
from database import db  # Importar la instancia de SQLAlchemy
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
    
    # Verificar si el usuario ya existe
    user = User.query.filter_by(username=username).first()
    
    if user:
        flash('Username already exists. Please choose another one.', 'error')
        return redirect(url_for('register.register_page'))
    
    p = str(random.randint(int(pow(10, 20)), int(pow(10, 50))))
    g = random.randint(2, int(p))
    a = str(gen_key(int(p)))
    e = power(g, int(a), int(p))
    
    en_password, c1 = encrypt(password, int(p), e, g)
    
    new_user = User(username=username, password=str(en_password), p=p, a=a, c1=str(c1))
    db.session.add(new_user)
    db.session.commit()
    
    return render_template('register.html', success=True)  # Redirigir a la página de login después de un registro exitoso