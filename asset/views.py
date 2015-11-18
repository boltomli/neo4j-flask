from .models import User, get_recent_assets
from flask import Flask, request, session, redirect, url_for, render_template, flash

app = Flask(__name__)

@app.route('/')
def index():
    assets = get_recent_assets()
    return render_template('index.html', assets=assets)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if len(username) < 1:
            flash('Your username must be at least one character.')
        elif len(password) < 5:
            flash('Your password must be at least 5 characters.')
        elif not User(username).register(password):
            flash('A user with that username already exists.')
        else:
            session['username'] = username
            flash('Logged in.')
            return redirect(url_for('index'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not User(username).verify_password(password):
            flash('Invalid login.')
        else:
            session['username'] = username
            flash('Logged in.')
            return redirect(url_for('index'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out.')
    return redirect(url_for('index'))

@app.route('/add_asset', methods=['POST'])
def add_asset():
    name = request.form['name']
    asset_id = request.form['asset_id']
    specs = request.form['specs']

    if not name or not asset_id or not specs:
        if not name:
            flash('You must give your asset a nick name.')
        if not asset_id:
            flash('You must give your asset an ID.')
        if not specs:
            flash('You must give your asset at least one property.')
    else:
        User(session['username']).add_asset(name, asset_id, specs)

    return redirect(url_for('index'))

@app.route('/profile/<username>')
def profile(username):
    logged_in_username = session.get('username')
    user_being_viewed_username = username

    user_being_viewed = User(user_being_viewed_username)
    assets = user_being_viewed.get_assets()

    return render_template(
        'profile.html',
        username=username,
        assets=assets
    )
