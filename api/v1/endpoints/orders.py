#!/usr/bin/env python3
"""
The API for making, pdating and deleting orders
"""
import datetime
from api.v1 import api_endpoints
from flask import request, jsonify
from app.models.reservations import Reservation
from app.models.user import User
from app.models.tables import Table
from app.utils.Auth import ValidateToken
from bson import ObjectId



@api_endpoints.route('/reserve', methods=["POST"], strict_slashes=False)
def create_reservations():
    """
    Creates a reservation
    """
    token = request.cookies.get("access_token")
    payload = ValidateToken(token)

    email = payload.get('email')
    user = User.objects(email=email).first()
    owner_id = user.id
    if owner_id:
        pass
    else:
        return jsonify({"error": "Missing owner"}), 400
    
    data = request.get_json()

    reservation_time = data.get('reservation_time')
    if reservation_time:
        reservation_time = datetime.datetime.fromisoformat(reservation_time.replace("Z", "+00:00"))
    else:
        return jsonify({"error": "Missing Reservation Time"}), 400

    party_size = data.get('party_size')
    if party_size:
        pass
    else:
        return jsonify({"error": "Missing Party size"}), 400
    
    special_request = data.get('special_request')

    contact_number = data.get('contact')
    if contact_number:
        pass
    else:
        return jsonify({"error": "Missing Contact Number"}), 400


    doc = Table.objects(booked=False).first()

    if doc:
        table_number = doc.table_number
    else:
        return jsonify({"Error": "All tables have been reserved"}), 400

    try:
        reservation = Reservation(
            owner_id=str(owner_id),
            reservation_time=reservation_time,
            party_size=party_size,
            special_request=special_request,
            contact_number=contact_number,
            table_number=table_number
        )
        reservation.save()
        doc.update(booked=True)
        user.legacypoints += 10
        user.save()

        return jsonify({
            "message": "Reservation created successfully",
            "table_number": table_number,
            "res_id": str(reservation.id)
        })
    except Exception as e:
        return jsonify({"error": "Error creating your reservation"}), 500