from flask import Flask
from config import Config # importing the config class from config.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from logging.handlers import RotatingFileHandler
import logging
import os
app = Flask(__name__) # app variable creation and this file connects the whole app together
app.config.from_object(Config) # this method is used to take the value from the object variable  
login = LoginManager(app)
login.login_view='login' # the input will be the endpoint as the same as the value passed in url_for()
db = SQLAlchemy(app) # database object for sqlALchemy database engine 
migrate = Migrate(app , db) # migirate object for migrate engine  
if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir("logs")
    file_handler = RotatingFileHandler('logs/Enclosure.log' , maxBytes=10240 , backupCount=10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Enclosure startup')
from app import routes ,model, errors
