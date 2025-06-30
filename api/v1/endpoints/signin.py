#!/usr/bin/env python3
"""
Sign in  endpoint
"""
import bcrypt
from api.v1 import api_endpoints
from flask import jsonify, request, make_response
from app.models.user import User
from app.utils.Auth import genToken


@api_endpoints.route("/signin", methods=["POST"], strict_slashes=False)
def Signin():
    """
    Handles Sign in
    """
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    email = email.strip().lower()

    if not email or not password:
        return jsonify({"error": "Missing Email or Password"}), 400

    doc = User.objects(email=email).first()

    if doc:
        correct = bcrypt.checkpw(password.encode(), doc.password.encode())

        print (correct)
        if correct:
            token = genToken(email)
            response = make_response(jsonify({"message": "Login successfull"}))
            response.set_cookie('access_token', token, max_age=604800, httponly=True, samesite='Strict')
            return response
        else:
            return jsonify({"error": "Incorrect email or password"}), 400
        
    else:
        return jsonify({"error": "Incorrect email or password"}), 400
