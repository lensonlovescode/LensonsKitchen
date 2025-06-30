#!/usr/bin/python3
"""
The route for the home page
"""
from app.pages import app_pages
from flask import render_template


@app_pages.route('/', strict_slashes=False)
def home():
    return render_template('home.html')
