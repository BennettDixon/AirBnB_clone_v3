#!/usr/bin/python3
"""
handles REST API actions for Place Amenity
"""
from api.v1.views import app_views
from os import getenv
from flask import jsonify
from flask import Flask
from flask import request
from flask import abort
from models import storage
from models.place import Place
from models.amenity import Amenity


@app_views.route(
    '/places/<string:place_id>/amenities',
    methods=['GET'],
    strict_slashes=False)
def place_amenity(place_id):
    """handles amenities route"""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        place.amenities
        return jsonify(place.amenity_ids)
    return jsonify([p_a.to_dict() for p_a in place.amenities])


@app_views.route(
    '/places/<string:place_id>/amenities/<string:amenity_id>',
    methods=['POST'],
    strict_slashes=False)
def place_amenity_post(place_id, amenity_id):
    place = storage.get("Place", place_id)
    amenity = storage.get("Amenity", amenity_id)
    if place is None or amenity is None:
        abort(404)
    if amenities.place_id == place_id:
        return jsonify(amenity.to_dict()), 200
    setattr(amenity, 'place_id', place_id)
    if getev('HBNB_TYPE_STORAGE') != db:
        place.amenties
        place.amenity_ids.append(amenity_id)
    return jsonify(amenity.to_dict()), 201


@app_views.route(
    '/places/<string:place_id>/amenities/<string:amenity_id>',
    methods=['DELETE'],
    strict_slashes=False)
def place_amenity_with_id(place_id, amenity_id):
    """handles amenities route with a parameter amenity_id"""
    amenity = storage.get("Amenity", amenity_id)
    place = storage.get("Place", place_id)
    if place is None or amenity is None:
        abort(404)
    if amenity.place_id != place_id:
        abort(404)
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        place.amenities
        if amenity_id in place.amenity_ids:
            place.amenity_ids.pop(amenity_id)
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200
