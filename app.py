from flask import Flask, render_template, url_for, g, request, redirect, flash, abort
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '47cb68fb89b29cc726f0cee40ae569a3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://database.db'
app.config['SQLALCHEMY_ECHO'] = True

login_manager = LoginManager()
db = SQLAlchemy()

login_manager.init_app(app)
db.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('login'))

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html');


if __name__ == '__main__':
    app.run(debug=True)
