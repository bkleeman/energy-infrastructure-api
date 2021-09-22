from flask import Blueprint
from flask import json
from flask.json import jsonify
import shotgun_api
from shotgun_api.constants import URL_PREFIX
from shotgun_api import *

bp = Blueprint('example_blueprint', __name__,
                                url_prefix=URL_PREFIX)

# @bp.route('/')
# def index():
#     resources = shotgun_api.db.infrastructure.find(projection = {"_id": False})
#     print('test index')
#     return jsonify([resource for resource in resources])


@bp.route('<primary_type>/')
def get_by_primary_type(primary_type):
    infrastructure = shotgun_api.db.infrastructure.find({'properties.type.primary': primary_type}, projection = {'_id': False}) 
    response = jsonify([resource for resource in infrastructure])
    response.headers.add("Access-Control-Allow-Origin", "*")
    print('test primary_type')
    return response

@bp.route("<primary_type>/<secondary_type>")
def get_infrastructure(primary_type, secondary_type):
    infrastructure = ''
    if primary_type == 'null':
        infrastructure = shotgun_api.db.infrastructure.find({'properties.type.secondary': secondary_type}, projection = {'_id': False})
    else:
        infrastructure = shotgun_api.db.infrastructure.find({"$and": [{'properties.type.primary': primary_type},{'properties.type.secondary': secondary_type}]}, projection = {"_id": False})    
    
    response = jsonify([resource for resource in infrastructure])
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response