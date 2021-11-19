from flask import Flask
from flask_pymongo import PyMongo
from flask_caching import Cache
from shotgun_api.constants import MONGO, URI, URL_PREFIX
from shotgun_api.example_bluprint import *

app = Flask(__name__)

app.register_blueprint(bp)

cache.init_app(app)

app.config["MONGO_URI"] = URI
mongodb_client = PyMongo(app)
db = mongodb_client.db