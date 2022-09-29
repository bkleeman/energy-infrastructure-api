from unittest.result import failfast
import requests

MINES_ENDPOINT = 'http://127.0.0.1:5000/api/v0.1.0/infrastructure/2012/mines/coal'
RAILROADS_ENDPOINT = 'http://127.0.0.1:5000/api/v0.1.0/infrastructure/2012/railroads'

def test_status_code():
    response = requests.get(MINES_ENDPOINT)
    assert response.status_code == 200

def test_verify_json(): 
    response = requests.get(MINES_ENDPOINT)
    assert response.headers["Content-Type"] == 'application/json'

def test_primary_type():
    response = requests.get(MINES_ENDPOINT)
    response_body = response.json()
    assert response_body['features'][0]['properties']['type']['primary'] == 'mines'

def test_secondary_type():
    response = requests.get(MINES_ENDPOINT)
    response_body = response.json()
    assert response_body['features'][0]['properties']['type']['secondary'] == 'coal'

def test_has_coordinates():
    response = requests.get(MINES_ENDPOINT)
    response_body = response.json()
    coords_exists = False
    if 'coordinates' in response_body['features'][0]['geometry']:
        coords_exists = True
    assert True

def test_primary_type_exclusive():
    response = requests.get(RAILROADS_ENDPOINT)
    response_body = response.json()
    assert response_body['features'][0]['properties']['type']['primary'] == 'railroads'

def test_primary_type_exclusive_status_code():
    response = requests.get(RAILROADS_ENDPOINT)
    assert response.status_code == 200