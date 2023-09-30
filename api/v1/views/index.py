#!/usr/bin/python3
'''index view for the API.'''
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def get_status():
    '''API status.
    '''
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def get_stats():
    '''number of objects for each type.
    '''
    return jsonify({
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
        })
