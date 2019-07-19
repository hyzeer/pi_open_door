from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from openDoor import config

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'rp'
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI

from openDoor import models, views