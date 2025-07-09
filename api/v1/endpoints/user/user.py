#!/usr/bin/env python3
"""
Endpoint to manage a user like updating their data and whatnot
"""
from api.v1 import api_endpoints
from flask import jsonify
from app.models.user import User
from flask import jsonify, request
from app.utils.Auth import ValidateToken
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'app/static/images'


@api_endpoints.route("/editpfp", methods=['PUT'], strict_slashes=False)
def edit_profile():
    """
    Updates a user profile
    """
    token = request.cookies.get("access_token")
    payload = ValidateToken(token)
    if not payload:
        return jsonify({"error": "Unauthorized"}), 401

    user = User.objects(email=payload['email']).first()
    if not user:
        print(payload['email'])
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    if 'FirstName' in data:
        user.FirstName = data['FirstName']
    if 'LastName' in data:
        user.LastName = data['LastName']
    if 'image_url' in data:
        user.image_url = data['image_url']

    user.save()
    return jsonify({"message": "Profile updated successfully"})


@api_endpoints.route('/uploadpfp', methods=['POST'])
def upload_pfp():
    token = request.cookies.get("access_token")
    payload = ValidateToken(token)
    if not payload:
        return jsonify({"error": "Unauthorized"}), 401

    if 'profilePic' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['profilePic']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    filename = secure_filename(file.filename)
    file.save(os.path.join(UPLOAD_FOLDER, filename))

    user = User.objects(email=payload['email']).first()
    user.image_url = f'/static/images/{filename}'
    user.save()

    return jsonify({"message": "Profile picture uploaded successfully", "url": user.image_url})
