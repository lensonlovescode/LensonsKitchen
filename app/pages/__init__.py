#!/usr/bin/env python3
"""
Registers all the blueprints when pages module is imported
"""
from flask import Blueprint

app_pages = Blueprint('app_pages', __name__, url_prefix='/')

from app.pages.signup import *
