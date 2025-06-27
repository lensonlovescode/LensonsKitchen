#!/usr/bin/env python3
"""
Status endpoint
package-lock.json
"""
from api.v1 import api_endpoints
from flask import jsonify

@api_endpoints.route("/status", strict_slashes=False)
def status():
    """
    Returns the status of the API
    """
    return jsonify({"Status": "OK"})
