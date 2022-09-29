from unittest.result import failfast
import requests

year = 2012

MINES_ENDPOINT = f'http://127.0.0.1:5000/api/v0.1.0/infrastructure/{year}/mines/coal'
RAILROADS_ENDPOINT = f'http://127.0.0.1:5000/api/v0.1.0/infrastructure/{year}/railroads'
GAS_WELLS_ENDPOINT = f'http://127.0.0.1:5000/api/v0.1.0/infrastructure/{year}/wells/gas'
OIL_WELLS_ENDPOINT = f'http://127.0.0.1:5000/api/v0.1.0/infrastructure/{year}/wells/oil'

# Helper functions
def check_status_code(endpoint):
    response = requests.get(endpoint)
    assert response.status_code == 200

def verify_json(endpoint): 
    response = requests.get(endpoint)
    assert response.headers["Content-Type"] == 'application/json'

def check_primary_type(endpoint, primary_type):
    response = requests.get(endpoint)
    response_body = response.json()
    assert response_body['features'][0]['properties']['type']['primary'] == primary_type

def check_secondary_type(endpoint, secondary_type):
    response = requests.get(endpoint)
    response_body = response.json()
    assert response_body['features'][0]['properties']['type']['secondary'] == secondary_type

def check_has_coordinates(endpoint):
    response = requests.get(endpoint)
    response_body = response.json()
    coords_exists = False
    if 'coordinates' in response_body['features'][0]['geometry']:
        coords_exists = True
    assert True

# Primary type exclusive tests, using railroads

def test_primary_type_exclusive():
    response = requests.get(RAILROADS_ENDPOINT)
    response_body = response.json()
    assert response_body['features'][0]['properties']['type']['primary'] == 'railroads'

def test_primary_type_exclusive_status_code():
    response = requests.get(RAILROADS_ENDPOINT)
    assert response.status_code == 200

# Mines tests

def test_status_code_mines():
    check_status_code(MINES_ENDPOINT)

def test_verify_json_mines():
    verify_json(MINES_ENDPOINT)

def test_primary_type_mines():
    check_primary_type(MINES_ENDPOINT, 'mines')

def test_secondary_type_mines():
    check_secondary_type(MINES_ENDPOINT, 'coal')

def test_has_coordinates_mines():
    check_has_coordinates(MINES_ENDPOINT)

# Gas wells tests

def test_gas_wells_status_code():
    response = requests.get(GAS_WELLS_ENDPOINT)
    assert response.status_code == 200

def test_primary_type_gas_wells():
    response = requests.get(GAS_WELLS_ENDPOINT)
    response_body = response.json()
    assert response_body['features'][0]['properties']['type']['primary'] == 'wells'

def test_secondary_type_gas_wells():
    response = requests.get(GAS_WELLS_ENDPOINT)
    response_body = response.json()
    assert response_body['features'][0]['properties']['type']['secondary'] == 'gas'

# Oil wells tests

def test_oil_wells_status_code():
    response = requests.get(GAS_WELLS_ENDPOINT)
    assert response.status_code == 200

def test_primary_type_oil_wells():
    response = requests.get(GAS_WELLS_ENDPOINT)
    response_body = response.json()
    assert response_body['features'][0]['properties']['type']['primary'] == 'wells'

def test_secondary_type_oil_wells():
    response = requests.get(GAS_WELLS_ENDPOINT)
    response_body = response.json()
    assert response_body['features'][0]['properties']['type']['secondary'] == 'gas'