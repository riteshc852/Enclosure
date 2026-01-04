# this file provides the routes 
from app import app # this is the app variable of flask from __init__.py
from flask import render_template, request , flash , redirect ,url_for
from app.forms import LoginForm , RegestrationForm 
from app import db
from app.model import users
from flask_login import current_user , login_user , logout_user , login_required
from urllib.parse import urlsplit
import sqlalchemy as sa
@app.route("/")
@app.route('/index')
@login_required
def index():
    user = {"username" : "ritesh"}
    posts = [
        {
            "author" : {"username" : "mike"},
            "body"  : "beautiful day in boston"
        },
        {
            "author" : {"username" : "harvey"},
            "body"  : "beautiful day in nyc"
        }
    ]
    # this posts should be same as the posts in jinja 2 template 
    return render_template("index.html" , title = "Home" , posts = posts)
@app.route("/register" , methods=["GET" , "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegestrationForm()
    if form.validate_on_submit(): #this method checks if the method is post and is validators true
        user = users(username=form.username.data , email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulation you are now registered")
        return redirect(url_for("login"))
    return render_template("register.html" , title="Register" , form=form )
@app.route("/login", methods=["GET" , "POST"])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
        sa.select(users).where(users.username == form.username.data))
        if user is None or not user.password_check(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc!="":
            next_page = url_for('index')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
    
