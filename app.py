"""
Info to Knowledge; Demonstration Web App
Python, Flask, MatPlotLib, Numpy, more
Clinton Garwood
License: MIT
September 2024
"""

import matplotlib.pyplot as plt
from flask import Flask, render_template, request, redirect, url_for, flash
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
# app.secret_key = 'secretkey'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.getcwd()), 'users.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

#
# class User(UserMixin, db.Model):
#     __tablename__ = 'users'  # Ensure this is set correctly
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(150), unique=True, nullable=False)
#     password = db.Column(db.String(150), nullable=False)
#
#
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         user = User.query.filter_by(username=username).first()
#         if user and check_password_hash(user.password, password):
#             login_user(user)
#             return redirect(url_for('dashboard'))
#         else:
#             flash('Login failed. Please check your username and password.')
#     return render_template('login.html')
#
#
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
#         new_user = User(username=username, password=hashed_password)
#         db.session.add(new_user)
#         db.session.commit()
#         flash('Registration successful. Please log in.')
#         return redirect(url_for('login'))
#     return render_template('register.html')
#
#
# @app.route('/dashboard')
# @login_required
# def dashboard():
#     return f"Hello, {current_user.username}! Welcome to your dashboard."
#
#
# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('login'))
#
#
# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()  # Create tables if they don't exist
#     app.run(debug=True)
#


@app.route('/')
@app.route('/index')
@app.route('/home')
def app_index():  # put application's code here
    return render_template("index.html")


@app.route('/success', methods=['GET'])
def get_success():
    return render_template('success.html')


@app.route('/form')
def web_form():
    return render_template('web_form.html')


@app.route('/results', methods=['GET'])
def results():
    return render_template('results.html')


@app.route('/results', methods=['POST'])
def post_success():
    # data = dict()
    starting = request.form['start_at']
    ending = request.form['end_at']

    # Generate a simple plot with the input range
    x = list(range(int(starting), int(ending) + 1))
    y = [i**2 for i in x]  # Example plot: y = x^2

    do_scatter(x, y)

    # Line Plot and save image
    plt.figure()
    plt.plot(x, y)
    plt.title(f'Plot for range x^2')
    plt.xlabel('Value as X')
    plt.ylabel('Value as x-squared x^2')
    plt.grid(True)
    # File path/name
    image_path = os.path.join('./static/img', 'plot.png')
    # Save image to the static/images directory
    plt.savefig(image_path)
    plt.close()

    # Bar Plot
    plt.bar(x, y)
    plt.title('Bar Plot: y = x^2')
    plt.xlabel('Value as X')
    plt.ylabel('Value as x-squared x^2')
    plt.grid(True)
    # File path/name
    image_path = os.path.join('./static/img/', 'bar_plot.png')
    # Save image to the static/images directory
    plt.savefig(image_path)
    plt.close()

    # Step Plot
    plt.step(x, y, where='mid')
    plt.title('Step Plot: y = x^2')
    plt.xlabel('Value as X')
    plt.ylabel('Value as x-squared x^2')
    plt.grid(True)
    # File path/name
    image_path = os.path.join('./static/img/', 'step_plot.png')
    # Save image to the static/images directory
    plt.savefig(image_path)
    plt.close()

    return render_template('web_form.html')


def do_scatter(x, y):
    # Scatter Plot
    plt.scatter(x, y)
    plt.title('Scatter Plot: y = x^2')
    plt.xlabel('Value as X')
    plt.ylabel('Value as x-squared x^2')
    plt.grid(True)
    # File path/name
    image_path = os.path.join('./static/img/', 'scatter_plot.png')
    # Save image to the static/images directory
    print(f'{image_path}')
    plt.savefig(image_path)
    plt.close()
    return


if __name__ == '__main__':
        # db.create_all()  # Create tables if they don't exist
    app.run(debug=True)
