from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
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
    cursor = connection.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            p TEXT NOT NULL,
            a TEXT NOT NULL,
            c1 TEXT NOT NULL
        );
    """)
    
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    
    if user:
        flash('Username already exists. Please choose another one.', 'error')
        return redirect(url_for('register.register_page'))
    
    p = str(random.randint(int(pow(10, 20)), int(pow(10, 50))))
    g = random.randint(2, int(p))
    a = str(gen_key(int(p)))
    e = power(g, int(a), int(p))
    
    en_password, c1 = encrypt(password, int(p), e, g)
    
    cursor.execute(
        "INSERT INTO users (username, password, p, a, c1) VALUES (?, ?, ?, ?, ?)",
        (username, str(en_password), p, a, str(c1))
    )
    connection.commit()
    cursor.close()
    connection.close()
    
    return render_template('register.html', success=True)