import flask
from flask import Flask #originial
from config import Config
#from flask_shelve import init_app
import os
app = Flask(__name__, static_url_path='')#original
app.config.from_object(Config)




from app import routes
