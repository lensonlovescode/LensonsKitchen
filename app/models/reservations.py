#!/usr/bin/env python3
"""
The reservations schema is defined in this module
"""
from mongoengine import Document, StringField, IntField, DateTimeField, BooleanField
import datetime


class Reservation(Document):
    """
    Represents a reservation, the class inherits from Document
    """
    owner_id = StringField(required=False)
    status = StringField(choices=['pending', 'confirmed', 'checked_in', 'cancelled', 'no_show'], default='pending')
    created_at = DateTimeField(default=datetime.datetime.utcnow())
    updated_at = DateTimeField(default=datetime.datetime.utcnow())
    reservation_time = DateTimeField()
    party_size = IntField(required=True)
    special_request = StringField(required=False)
    table_number = IntField(required=False)
    has_order = BooleanField(default=False)
    order_id = StringField(required=False)
    contact_number = StringField(required=True)
