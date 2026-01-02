from flask import Flask
from config import Config # importing the config class from config.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__) # app variable creation and this file connects the whole app together
app.config.from_object(Config) # this method is used to take the value from the object variable  
db = SQLAlchemy(app) # database object for sqlALchemy database engine 
migrate = Migrate(app , db) # migirate object for migrate engine  
from app import routes ,model
