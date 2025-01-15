import os
from flask import Flask
from dotenv import load_dotenv
from flask_pymongo import PyMongo


#Load env variables
load_dotenv()

#Init flask RESTful API
app = Flask(__name__)

#API config
app.config["MONGO_URI"] = os.getenv("CONNECTION_STRING")

#Init MongoDB
mongo = PyMongo(app)

#Import Routes
from api import routes
