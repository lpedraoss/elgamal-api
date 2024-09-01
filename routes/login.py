from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from database import get_db_connection
from utils.encryption import verify_password

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/login', methods=['GET', 'POST'])
# def login_page():
#     return render_template('login.html')

# @login_blueprint.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        try:
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)
        
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
            
            if user and verify_password(password, eval(user['password']), int(user['p']), int(user['a']), int(user['c1'])):
                cursor.close()
                connection.close()
                return redirect(url_for('home_page'))
            else:
                flash('Login failed. Check your username and/or password.', 'error')
                return redirect(url_for('login.login'))
        except Exception as e:
            flash(f'An error occurred: {e}', 'error')
            return redirect(url_for('login.login'))
            
        finally:
            cursor.close()
            connection.close()
    
    return render_template('login.html')