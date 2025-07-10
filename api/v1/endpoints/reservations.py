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


@api_endpoints.route('/delres/<res_id>', methods=['DELETE'], strict_slashes=False)
def delete_reservation(res_id):
    """
    Deletes a reservation and frees the table
    """
    doc = Reservation.objects(id=res_id).first()
    if not doc:
        return jsonify({"error": "Reservation does not exist"}), 404

    table = Table.objects(table_number=doc.table_number).first()
    if table:
        table.booked = False
        table.save()

    doc.delete()
    return jsonify({"message": "Reservation deleted successfully"})


@api_endpoints.route('/upres/<res_id>', methods=['PUT'], strict_slashes=False)
def update_reservation(res_id):
    """
    Updates a reservation, based on the reservation id
    """
    data = request.get_json()

    doc = Reservation.objects(id=res_id).first()
    if not doc:
        return jsonify({"error": "Reservation does not exist"}), 404

    updatable_fields = [
        "status", "reservation_time", "party_size", "special_request",
        "table_number", "has_order", "order_id"
    ]

    for field in updatable_fields:
        if field in data:
            if field == "reservation_time":
                data[field] = datetime.datetime.fromisoformat(data[field])
            setattr(doc, field, data[field])

    doc.updated_at = datetime.datetime.utcnow()
    doc.save()

    if doc.status == "checked_in":
        table = Table.objects(table_number=doc.table_number).first()
        if table:
            table.booked = False
            table.save()

    return jsonify({"message": "Reservation updated successfully"})



@api_endpoints.route('/reservation/<res_id>')
def get_reservation(res_id):
    """
    Gets a specific reservation based on the ID
    """
    res = Reservation.objects(id=ObjectId(res_id)).first()

    return jsonify({res.to_mongo().to_dict()})
    

@api_endpoints.route('/reservations/<user_id>')
def get_my_reservations(user_id):
    """
    Gets all reservations belonging to a specific user based on their id
    """
    res_list = Reservation.objects(owner_id=user_id)

    reservations = []
    for r in res_list:
        res_dict = r.to_mongo().to_dict()
        res_dict['_id'] = str(res_dict['_id'])
        if 'order_id' in res_dict:
            res_dict['order_id'] = str(res_dict['order_id'])
        reservations.append(res_dict)

    if reservations:
        return jsonify(reservations)
    else:
        return jsonify({"error": "No reservations found"}), 404



@api_endpoints.route('/allreservations')
def get_all_reservations():
    """
    Gets all reservations with user info
    """
    res = Reservation.objects()
    reservations = []

    for r in res:
        reservation = r.to_mongo().to_dict()
        reservation['_id'] = str(reservation['_id'])

        user = User.objects(id=reservation['owner_id']).first()
        if user:
            reservation['user_info'] = {
                'email': user.email,
                'FirstName': user.FirstName,
                'LastName': user.LastName,
                'status': user.status
            }
        else:
            reservation['user_info'] = None

        reservations.append(reservation)

    return jsonify(reservations)


@api_endpoints.route('/pendreservations')
def get_pending_reservations():
    """
    Gets all pending reservations with user info
    """
    res = Reservation.objects(status="pending")
    reservations = []

    for r in res:
        reservation = r.to_mongo().to_dict()
        reservation['_id'] = str(reservation['_id'])

        user = User.objects(id=reservation['owner_id']).first()
        if user:
            reservation['user_info'] = {
                'email': user.email,
                'FirstName': user.FirstName,
                'LastName': user.LastName,
                'status': user.status
            }
        else:
            reservation['user_info'] = None

        reservations.append(reservation)

    return jsonify(reservations)
