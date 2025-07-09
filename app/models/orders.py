#!/usr/bin/env python3
"""
The reservations schema is defined in this module
"""
from mongoengine import Document, StringField, DateTimeField, BooleanField
import datetime


class Order(Document):
    """
    Represents an order, the class inherits from Document
    """
    Owner_id = StringField(required=False)
    status = StringField(choices=['pending', 'confirmed', 'checked_in', 'cancelled', 'no_show'], default='pending')
    created_at = DateTimeField(default=datetime.datetime.utcnow)
    updated_at = DateTimeField(default=datetime.datetime.utcnow)
    is_paid - BooleanField(default=False)
