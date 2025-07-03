#!/usr/bin/env python3
"""
The user schema is defined in this module
"""
from mongoengine import Document, StringField, EmailField, DateTimeField, IntField
import datetime


class User(Document):
    """
    Represents a user, the class inherits from Document
    """
    FirstName = StringField(required=False)
    LastName = StringField(required=False)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    legacypoints = IntField(default=0)
    status = StringField(choices=['Bronze', 'Gold', 'Diamond', 'Platnum'], default='Bronze')
    created_at = DateTimeField(default=datetime.datetime.utcnow)
