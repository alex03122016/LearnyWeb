import flask
from flask import Flask #originial
from config import Config
#from flask_shelve import init_app
import os
from flask_caching import Cache
app = Flask(__name__, static_url_path='')#original
app.config.from_object(Config)
# Check Configuring Flask-Cache section for more details
cache = Cache(app,config={'CACHE_TYPE': 'simple'})



from app import routes
