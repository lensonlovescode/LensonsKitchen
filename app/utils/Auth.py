#!/usr/bin/env python3
"""
Contains the authentication stuff, mostly the JWT tokens handlers
"""
import os
import jwt
import datetime


def genToken(Email):
    """
    Generates the JWT token
    """
    SECRET_KEY = os.getenv("SK")

    payload = {
        "email": Email,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=168)
    }

    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def ValidateToken(token):
    """
    Validates the validity of an access token
    """
    SECRET_KEY = os.getenv("SK")
    try:
        decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded_payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError as e:
        return None
