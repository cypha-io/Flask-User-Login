from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user
from app import app, db
from app.models import User
from app.forms import RegistrationForm, LoginForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        flash('Registration success! You can now login.', 'Success')
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=[('GET', 'POST')])
def login():
    if request.method == 'POST':
        flash('Login Sucessful!', 'Success')
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    flash('You have successfully logged out!')
    return redirect(url_for('index'))

@app.route('/admin')
def admin():
    if not current_user.is_authenticated or not current_user.is_admin:
        return redirect(url_for('index'))
    return redirect(url_for('admin.index'))
