"""Routes and data fed to Flask to generate webpages"""

from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/home')
def home():
    """Website homepage with spell/book search"""
    user = {'username': 'Quentin'}
    return render_template('home.html', title='Home', user=user)

@app.route('/search')
def search():
    """Advanced search function with filters"""
    return render_template('base.html', title='Search')

@app.route('/profile')
def profile():
    """Website homepage with spell/book search"""
    return render_template('base.html', title='Spellbook Profile')

@app.route('/spellbooks')
def spellbooks():
    """Website homepage with spell/book search"""
    return render_template('base.html', title='Spellbooks')

@app.route('/spells')
def spells():
    """Website homepage with spell/book search"""
    return render_template('base.html', title='Spells')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login/Signup form page"""
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember me = {}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('home'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/settings')
def settings():
    """Account settings"""
    return render_template('base.html', title='Account Settings')
