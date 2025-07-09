#!/usr/bin/python3
"""
The route for the profile page
"""
from app.pages import app_pages
from flask import render_template


@app_pages.route('/profile', strict_slashes=False)
def profile():
    return render_template('profile.html')