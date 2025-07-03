#!/usr/bin/env python3
"""
The API for making, pdating and deleting reservations
"""
import datetime
from api.v1 import api_endpoints
from flask import request, jsonify
from app.models.reservations import Reservation
from app.models.user import User
from app.models.tables import Table
from app.utils.Auth import ValidateToken


@api_endpoints.route('/reserve', methods=["POST"], strict_slashes=False)
def create_reservations():
    """
    Creates a reservation
    """
    token = request.cookies.get("access_token")
    payload = ValidateToken(token)

    email = payload.get('email')
    doc = User.objects(email=email).first()
    owner_id = doc.id
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
        return jsonify({"Error": "All tables have been reserved"})

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
        return jsonify({
            "message": "Reservation created successfully",
            "table_number": table_number,
            "res_id": str(reservation.id)
        })
    except Exception as e:
        return jsonify({"error": "Error creating your reservation"}), 500


@api_endpoints.route('/delres/<res_id>', methods=['DELETE'], strict_slashes=False)
def delete_reservation(res_id):
    """
    Deletes a reservation
    """
    doc = Reservation.objects(reservation_id=res_id).first()

    if doc:
        doc.delete()
        return jsonify({"message": "Reservation deleted successfully"})
    else:
        return jsonify({"error": "Reservation Does not exist"}), 404


@api_endpoints.route('upres/res_id', methods=['PUT'], strict_slashes=False)
def update_reservation(res_id):
    """
    Updates a reservation, based on the reservation id
    """
    data = request.get_json()

    owner_id = data.get("owner_id")

    doc = Reservation.objects(reservation_id=res_id, owner_id=owner_id).first()

    if not doc:
        return jsonify({"error": "Reservation does not exist"}), 404

    updatable_fields = [
        "status", "reservation_time", "party_size", "special_request",
        "table_number", "has_order", "order_id"
    ]

    for field in updatable_fields:
        if field in data:
            setattr(doc, field, data[field])

    doc.updated_at = datetime.datetime.utcnow()
    doc.save()

    return jsonify({"message": "Reservation updated successfully"})


@api_endpoints.route('/reservation/<res_id>')
def get_reservation(res_id):
    """
    Gets a specific reservation based on the ID
    """
    res = Reservation.objects(_id=res_id)
    return jsonify({res.to_mongo().to_dict()})
    

@api_endpoints.route('/reservations/<user_id>')
def get_my_reservations(user_id):
    """
    Gets all reservations belonging to a specific user based on their id
    """
    res_list = Reservation.objects(owner_id=user_id)

    if res_list:
        return jsonify([r.to_mongo().to_dict() for r in res_list])
    else:
        return jsonify({"error": "No reservations found"}), 404

