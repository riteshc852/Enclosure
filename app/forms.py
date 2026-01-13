from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField ,SubmitField 
from wtforms.validators import DataRequired ,Email , EqualTo , ValidationError ,Length
from app import db
from app.model import users
import sqlalchemy as sa
class RegestrationForm(FlaskForm):
    username = StringField("username" , validators=[DataRequired()])
    email = StringField("Email" , validators=[DataRequired() , Email()] )
    password = PasswordField("password" , validators=[DataRequired()])
    password2 = PasswordField("Repeat Password" , validators=[DataRequired() , EqualTo("password")])
    submit = SubmitField("Register")
    def validate_username(self ,username):
        user = db.session.scalar(sa.select(users).where(users.username == username.data))
        if user is not None:
            raise ValidationError("Please use diffrent username")
    def validate_email(self , email):
        user = db.session.scalar(sa.select(users).where(users.email == email.data))
        if user is not None:
            raise ValidationError("Please use diffrent email")  
class LoginForm(FlaskForm):
    username = StringField("username" , validators=[DataRequired()])
    password = PasswordField("password" , validators=[DataRequired()])
    remember_me= BooleanField("Remember me")
    submit = SubmitField("Sign in")
class ProfileEditForm(FlaskForm):
    username = StringField("username" , validators=[DataRequired()])
    about_me = TextAreaField("About me" , validators=[Length(min=0 , max=140)])
    submit = SubmitField("Submit")