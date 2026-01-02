# this file defines the configuration of the app (provides data to the app)
import os
from dotenv import load_dotenv
#  this give the folder and path of the app 
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()
class Config :
    SECRET_KEY= os.getenv("SECRET_KEY")
    # here the os method is used because if the traditional method used there is no backup
    # plan for app if the uri doesnt exist 
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False