# this file provides the routes 
from app import app # this is the app variable of flask from __init__.py
from flask import render_template, request , flash , redirect ,url_for
from app.forms import LoginForm
@app.route("/")
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
    return render_template("index.html" , title = "Home" , user = user , posts = posts)
@app.route("/login", methods=["GET" , "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login Requested for {} , remember_me{}".format(form.username.data , form.remember_me.data))
        return redirect(url_for("index")) # url for takes function name as input for endpoint 
    return render_template("login.html" , title ="Sign in" , form = form )
