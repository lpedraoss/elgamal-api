from flask import Blueprint, request, render_template, redirect, url_for, flash
from models.user import User  # Importar el modelo de usuario
from database import db  # Importar la instancia de SQLAlchemy
from utils.encryption import verify_password

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        try:
            user = User.query.filter_by(username=username).first()
            
            if user and verify_password(password, eval(user.password), int(user.p), int(user.a), int(user.c1)):
                return redirect(url_for('home_page'))
            else:
                flash('Login failed. Check your username and/or password.', 'error')
                return redirect(url_for('login.login'))
        except Exception as e:
            flash(f'An error occurred: {e}', 'error')
            return redirect(url_for('login.login'))
    
    return render_template('login.html')