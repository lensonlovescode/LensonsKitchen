#!/usr/bin/env python3
"""
Creates the API blueprints
"""
from flask import Blueprint

api_endpoints = Blueprint('api_endpoints', __name__, url_prefix='/api/v1')

from api.v1.endpoints.status import *
from api.v1.endpoints.signup import *
