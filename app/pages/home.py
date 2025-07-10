#!/usr/bin/python3
"""
The route for the home page
"""
from app.pages import app_pages
from flask import render_template


@app_pages.route('/', strict_slashes=False)
def home():
    return render_template('home.html')

@app_pages.route('/foodmenus', strict_slashes=False)
def foodmenus():
    return render_template('foodmenus.html')

@app_pages.route('/drinksmenus', strict_slashes=False)
def drinksmenus():
    return render_template('drinksmenus.html')

@app_pages.route('/offers', strict_slashes=False)
def offers():
    return render_template('offers.html')

@app_pages.route('/events', strict_slashes=False)
def weekly_events():
    return render_template('events.html')