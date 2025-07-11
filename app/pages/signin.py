#!/usr/bin/env python3
"""
Login page
"""
from app.pages import app_pages
from flask import render_template


@app_pages.route("/signin", strict_slashes=False)
def login_page():
    """
    Route for the login page
    """
    return render_template("signin.html")


@app_pages.route("/adminsignin", strict_slashes=False)
def admins_login_page():
    """
    Route for the login page for admins
    """
    return render_template("signinadmin.html")
