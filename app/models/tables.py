#!/usr/bin/env python3
"""
The Table schema is defined in this module
"""
from mongoengine import Document, StringField, BooleanField, IntField


class Table(Document):
    """
    Represents a table, the class inherits from Document
    """
    owner_id = StringField(required=False)
    table_number = IntField(required=True)
    table_size = IntField(required=True)
    booked = BooleanField(default=False)
