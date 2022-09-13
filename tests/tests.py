import requests

API_ENDPOINT_URL = 'http://127.0.0.1:5000/api/v0.1.0/infrastructure/mines/coal'

def test_status_code():
    response = requests.get(API_ENDPOINT_URL)
    assert response.status_code == 200

def test_verify_json(): 
    response = requests.get(API_ENDPOINT_URL)
    assert response.headers["Content-Type"] == 'application/json'

def test_primary_type():
    response = requests.get(API_ENDPOINT_URL)
    response_body = response.json()
    assert response_body['features']['properties']['type']['primary'] == 'mines'