#!/usr/bin/env python3
"""
Admin page
"""
from app.pages import app_pages
from flask import render_template


@app_pages.route("/admin", strict_slashes=False)
def admin_page():
    """
    Route for the admin page
    """
    return render_template("admin.html")
