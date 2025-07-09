#!/usr/bin/env python3
"""
Registers all the blueprints when pages module is imported
"""
from flask import Blueprint

app_pages = Blueprint('app_pages', __name__, url_prefix='/')

from app.pages.signup import *
from app.pages.home import *
from app.pages.signin import *
from app.pages.reserve import *
from app.pages.admin import *
from app.pages.profile import *
