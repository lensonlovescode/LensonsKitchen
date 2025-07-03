#!/usr/bin/python3
"""
The route for the reserve page
"""
from app.pages import app_pages
from flask import render_template


@app_pages.route('/reserve', strict_slashes=False)
def reserve():
    return render_template('reserve.html')
