#!/usr/bin/env python3
"""
Sign logout endpoint
"""
import bcrypt
from api.v1 import api_endpoints
from flask import jsonify, request, make_response
from app.utils.Auth import ValidateToken


@api_endpoints.route("/logout", strict_slashes=False)
def Sign_out():
    """
    Logs the user out
    """
    token = request.cookies.get("access_token")

    response = make_response(jsonify({"message": "Logout successfull"}))
    response.set_cookie('access_token', None, max_age=1, httponly=True, samesite='Strict')
    return response
