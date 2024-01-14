# app/__init__.py
from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # SQLite for user data
app.config['MONGO_URI'] = 'mongodb://localhost:27017/product_catalog'  # MongoDB for product data

db.init_app(app)
with app.app_context():
    db.create_all()
mongo = PyMongo(app)
from app import app_controller