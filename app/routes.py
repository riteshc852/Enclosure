# this file provides the routes 
from app import app # this is the app variable of flask from __init__.py
from flask import render_template, request , flash , redirect ,url_for
from app.forms import LoginForm , RegestrationForm , ProfileEditForm
from app import db
from app.model import users
from flask_login import current_user , login_user , logout_user , login_required
from datetime import datetime , timezone
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
@app.before_request # this function will constantly update time for every view function 
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now(timezone.utc)
        db.session.commit()
@app.route("/user/<username>")
@login_required
def user(username):
    user = db.first_or_404(sa.select(users).where(users.username == username))
    posts=[
        {"author" : user , "body" :"Test post 1"},
        {"author" : user , "body" :"Test post 2"} 
    ]
    return render_template("user.html", user=user , posts=posts  )
@app.route("/edit_profile" , methods=["GET" , "POST"])
@login_required
def edit_profile():
    form = ProfileEditForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash("Your changes Have been saved")
        return redirect(url_for("edit_profile"))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template("edit_profile.html" , title = "Edit Profile" , form = form)
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
    
