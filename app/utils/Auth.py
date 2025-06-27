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
