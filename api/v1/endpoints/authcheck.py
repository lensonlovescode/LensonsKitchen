#!/usr/bin/env python3
"""
Endpoint checks if user is logged in by checking for a valid access token
"""
from api.v1 import api_endpoints
from flask import jsonify, request
from app.utils.Auth import ValidateToken


@api_endpoints.route("/authcheck", methods=["GET"], strict_slashes=False)
def CheckLogin():
    """
    Checks if a user is logged in
    """
    token = request.cookies.get("access_token")
    payload = ValidateToken(token)

    if payload:
        return jsonify({"message": "Logged in"})
    else:
        return jsonify({"error": "Unauthorized"}), 401
