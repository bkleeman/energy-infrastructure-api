import flask
from flask import render_template
from flask import Blueprint
from flask import json
from flask.json import jsonify
import energy_infrastructure_api
from flask_caching import Cache
from energy_infrastructure_api.constants import URL_PREFIX
from energy_infrastructure_api.excluded_fields import EXCLUDED_FIELDS

bp = Blueprint('endpoints', __name__,
                                url_prefix=URL_PREFIX)

cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})

@bp.route('/')
def index():
    # resources = energy_infrastructure_api.db.infrastructure.find(projection = {"_id": False})
    # return jsonify([resource for resource in resources])
    return flask.render_template('index.html')


@bp.route('<int:nominal_year>/<primary_type>')
@cache.cached(timeout=3600000)
def get_by_primary_type(nominal_year, primary_type):
    # add a geospatial index to every collection based on the geometry field or coordinates or whatever
    # we want to use a 2dsphere, but check atlas db codebase for examples. Write a throwaway script for this
    # Filter out keys you don't want with projection values
    # Then worry about caching afterwards
    infrastructure = energy_infrastructure_api.db.infrastructure.find({"$and": [{'properties.required.years.nominal': nominal_year}, {'properties.type.primary': primary_type}]}, projection = EXCLUDED_FIELDS) 
    response = jsonify({ "type": "FeatureCollection",
                        "features": [resource for resource in infrastructure]})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@bp.route("<int:nominal_year>/<primary_type>/<secondary_type>")
@cache.cached(timeout=3600000)
def get_infrastructure(nominal_year, primary_type, secondary_type):
    infrastructure = ''
    if primary_type == 'null':
        infrastructure = energy_infrastructure_api.db.infrastructure.find({"$and": [{'properties.required.years.nominal': nominal_year}, {'properties.type.secondary': secondary_type}]}, projection = EXCLUDED_FIELDS)
    else:
        infrastructure = energy_infrastructure_api.db.infrastructure.find({"$and": [{'properties.required.years.nominal': nominal_year}, { 'properties.type.primary': primary_type},{ 'properties.type.secondary': secondary_type}]}, projection = EXCLUDED_FIELDS)    

    resources = [resource for resource in infrastructure]

    response = jsonify({ "type": "FeatureCollection",
                        "features": resources})
    response.headers.add("Access-Control-Allow-Origin", "*")
    
    return response