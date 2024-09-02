from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from database import get_db_connection
from utils.encryption import verify_password

login_blueprint = Blueprint('login', __name__)
@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        try:
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
            
            if user and verify_password(password, eval(user[2]), int(user[3]), int(user[4]), int(user[5])):
                return redirect(url_for('home_page'))
            else:
                flash('Login failed. Check your username and/or password.', 'error')
                return redirect(url_for('login.login'))
        except Exception as e:
            flash(f'An error occurred: {e}', 'error')
            return redirect(url_for('login.login'))
            
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
    
    return render_template('login.html')