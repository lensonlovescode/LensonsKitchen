#!/usr/bin/env python3
"""
Login page
"""
from app.pages import app_pages
from flask import render_template


@app_pages.route("login", strict_slashes=False)
def login_page():
    """
    Route for the login page
    """
    return render_template("login.html")
