#!/usr/bin/env python3
"""
Utility to hash the password
"""
import bcrypt


def hash_pwd(pwd):
    """
    Function to hash the password
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pwd.encode('utf-8'), salt)
    return hashed.decode('utf-8')
