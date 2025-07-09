#!/usr/bin/env python3
"""
Endpoint checks if user is logged in by checking for a valid access token
"""
from api.v1 import api_endpoints
from flask import jsonify, request
from app.utils.Auth import ValidateToken
from app.models.user import User


@api_endpoints.route("/authcheck", methods=["GET"], strict_slashes=False)
def CheckLogin():
    """
    Checks if a user is logged in
    """
    token = request.cookies.get("access_token")
    payload = ValidateToken(token)

    email = payload.get('email')
    print(email)

    print(type(payload))

    user = User.objects(email=email).first()

    payload['id'] = str(user.id)
    payload['FirstName'] = str(user.FirstName)
    payload['LastName'] = str(user.LastName)
    payload['LegacyPoints'] = str(user.legacypoints)
    payload['status'] = str(user.status)

    if payload:
        return jsonify({"message": "Logged in", "data": payload})
    else:
        return jsonify({"error": "Unauthorized"}), 401
    
@api_endpoints.route("/authcheckadmin", methods=["GET"], strict_slashes=False)
def CheckLoginAdmin():
    """
    Checks if a user is logged in and is admin
    """
    token = request.cookies.get("access_token")
    payload = ValidateToken(token)

    if not payload:
        return jsonify({"error": "Unauthorized"}), 401

    email = payload.get('email')
    user = User.objects(email=email).first()

    if not user or not user.admin:
        return jsonify({"error": "Forbidden: Admins only"}), 403

    payload['id'] = str(user.id)
    payload['FirstName'] = str(user.FirstName)
    payload['LastName'] = str(user.LastName)
    payload['LegacyPoints'] = str(user.legacypoints)
    payload['status'] = str(user.status)

    return jsonify({"message": "Logged in", "data": payload})
