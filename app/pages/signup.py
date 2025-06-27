#!/usr/bin/python3
"""
The route for the signup page
"""
from app.pages import app_pages
from flask import render_template


@app_pages.route('/signup', strict_slashes=False)
def signup_page():
    return render_template('signup.html')
