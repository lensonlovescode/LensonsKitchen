#!/usr/bin/env python3
"""
Signup endpoint
"""
from api.v1 import api_endpoints
from flask import jsonify, request, make_response
from app.utils.hash import hash_pwd
from app.models.user import User
from app.utils.Auth import genToken
from mongoengine.errors import ValidationError, NotUniqueError


@api_endpoints.route("/signup", methods=["POST"], strict_slashes=False)
def Signup():
    """
    Handles Sign up
    """
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Missing Email or Password"}), 400

    email = email.strip().lower()

    hashedPwd = hash_pwd(password)

    try:
        user = User(email=email, password=hashedPwd)
        user.save()

        token = genToken(email)

        response = make_response(jsonify({"message": "User created successfully"}))
        response.set_cookie('access_token', token, max_age=604800, httponly=True, samesite='Strict')

        return response
    
    except NotUniqueError:
        return jsonify({"error": "Email already exists"}), 409
    
    except ValidationError:
        return jsonify({"error": "Invalid data provided"}), 400
    
    except Exception as e:
        print(e)
        return jsonify({"error": "Internal server error"}), 500
