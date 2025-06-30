#!/usr/bin/env python3
"""
API module
"""
from flask import Flask
from flask_cors import CORS
from api.v1 import api_endpoints
from mongoengine import connect

app = Flask(__name__)
app.register_blueprint(api_endpoints)
cors = CORS(app, supports_credentials=True, resources={r"/*": {"origins": "http://localhost:5001"}})

connect('LensonsKitchen')

if __name__ == '__main__':
    app.run('localhost', 5000, debug=True)
