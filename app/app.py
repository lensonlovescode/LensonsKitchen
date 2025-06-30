#!/usr/bin/env python3
"""
Main Application
"""
from flask import Flask
from flask_cors import CORS
from app.pages import app_pages
from mongoengine import connect

app = Flask(__name__)
app.register_blueprint(app_pages)
cors = CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})

connect("LensonsKitchen")

if __name__ == '__main__':
    app.run('localhost', 5001, debug=True)
