#!/usr/bin/env python3
"""
The API for making, pdating and deleting reservations
"""
import datetime
from api.v1.endpoints import api_endpoints
from flask import request, jsonify
from app.models import Reservation, Table


@api_endpoints.route('/reserve', methods=["POST"], strict_slashes=False)
def create_reservations():
    """
    Creates a reservation
    """
    data = request.get_json()

    owner_id = data.get('owner')
    if owner_id:
        pass
    else:
        return jsonify({"error": "Missing owner"}), 400

    reservation_time = data.get('reservation_time')
    if reservation_time:
        reservation_time = datetime.fromisoformat(reservation_time.replace("Z", "+00:00"))
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
        return jsonify({"Error": "All tables have been reserved"})

    try:
        reservation = Reservation(
            owner_id=owner_id,
            reservation_time=reservation_time,
            party_size=party_size,
            special_request=special_request,
            contact_number=contact_number,
            table_number=table_number
        )
        reservation.save()
        doc.update(booked=True)
        return jsonify({"message": "Reservation created successfully", "table_number": table_number})
    except Exception as e:
        return jsonify({"error": "Error creating your reservation"}), 500
