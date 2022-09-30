from unittest.result import failfast
import requests

year = 2012

MINES_ENDPOINT = f'http://127.0.0.1:5000/api/v0.1.0/infrastructure/{year}/mines/coal'
RAILROADS_ENDPOINT = f'http://127.0.0.1:5000/api/v0.1.0/infrastructure/{year}/railroads'
GAS_WELLS_ENDPOINT = f'http://127.0.0.1:5000/api/v0.1.0/infrastructure/{year}/wells/gas'
OIL_WELLS_ENDPOINT = f'http://127.0.0.1:5000/api/v0.1.0/infrastructure/{year}/wells/oil'
GAS_PIPELINES_ENDPOINT = f'http://127.0.0.1:5000/api/v0.1.0/infrastructure/{year}/pipelines/gas'
OIL_PIPELINES_ENDPOINT = f'http://127.0.0.1:5000/api/v0.1.0/infrastructure/{year}/pipelines/oil'
PETROLEUM_PRODUCT_PIPELINES_ENDPOINT = f'http://127.0.0.1:5000/api/v0.1.0/infrastructure/{year}/pipelines/petroleum_product'
OIL_REFINERIES_ENDPOINT = f'http://127.0.0.1:5000/api/v0.1.0/infrastructure/{year}/refineries/petroleum'
GAS_PROCESSING_ENDPOINT = f'http://127.0.0.1:5000/api/v0.1.0/infrastructure/{year}/processing/gas'
COAL_PLANTS_ENDPOINT = f'http://127.0.0.1:5000/api/v0.1.0/infrastructure/{year}/power_plants/coal'
NATURAL_GAS_PLANTS_ENDPOINT = f'http://127.0.0.1:5000/api/v0.1.0/infrastructure/{year}/power_plants/natural_gas'
PETROLEUM_PLANTS_ENDPOINT = f'http://127.0.0.1:5000/api/v0.1.0/infrastructure/{year}/power_plants/petroleum'
NUCLEAR_PLANTS_ENDPOINT = f'http://127.0.0.1:5000/api/v0.1.0/infrastructure/{year}/power_plants/nuclear'
HYDROELECTRIC_PLANTS_ENDPOINT = f'http://127.0.0.1:5000/api/v0.1.0/infrastructure/{year}/power_plants/hydroelectric'
WIND_PLANTS_ENDPOINT = f'http://127.0.0.1:5000/api/v0.1.0/infrastructure/{year}/power_plants/wind'
SOLAR_PLANTS_ENDPOINT = f'http://127.0.0.1:5000/api/v0.1.0/infrastructure/{year}/power_plants/solar'
GEOTHERMAL_PLANTS_ENDPOINT = f'http://127.0.0.1:5000/api/v0.1.0/infrastructure/{year}/power_plants/geothermal'

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

# Railroad tests

def test_status_code_railroads():
    check_status_code(RAILROADS_ENDPOINT)

def test_verify_json_railroads():
    verify_json(RAILROADS_ENDPOINT)

def test_primary_type_railroads():
    check_primary_type(RAILROADS_ENDPOINT, 'railroads')

def test_has_coordinates_railroads():
    check_has_coordinates(RAILROADS_ENDPOINT)

# Gas wells tests

def test_status_code_gas_wells():
    check_status_code(GAS_WELLS_ENDPOINT)

def test_verify_json_gas_wells():
    verify_json(GAS_WELLS_ENDPOINT)

def test_primary_type_gas_wells():
    check_primary_type(GAS_WELLS_ENDPOINT, 'wells')

def test_secondary_type_gas_wells():
    check_secondary_type(GAS_WELLS_ENDPOINT, 'gas')

def test_has_coordinates_gas_wells():
    check_has_coordinates(GAS_WELLS_ENDPOINT)

# Oil wells tests

def test_status_code_oil_wells():
    check_status_code(OIL_WELLS_ENDPOINT)

def test_verify_json_oil_wells():
    verify_json(OIL_WELLS_ENDPOINT)

def test_primary_type_oil_wells():
    check_primary_type(OIL_WELLS_ENDPOINT, 'wells')

def test_secondary_type_oil_wells():
    check_secondary_type(OIL_WELLS_ENDPOINT, 'oil')

def test_has_coordinates_oil_wells():
    check_has_coordinates(OIL_WELLS_ENDPOINT)

# Gas pipelines tests

def test_status_code_gas_pipelines():
    check_status_code(GAS_PIPELINES_ENDPOINT)

def test_verify_json_gas_pipelines():
    verify_json(GAS_PIPELINES_ENDPOINT)

def test_primary_type_gas_pipelines():
    check_primary_type(GAS_PIPELINES_ENDPOINT, 'pipelines')

def test_secondary_type_gas_pipelines():
    check_secondary_type(GAS_PIPELINES_ENDPOINT, 'gas')

def test_has_coordinates_gas_pipelines():
    check_has_coordinates(GAS_PIPELINES_ENDPOINT)

# Oil pipelines tests

def test_status_code_oil_pipelines():
    check_status_code(OIL_PIPELINES_ENDPOINT)

def test_verify_json_oil_pipelines():
    verify_json(OIL_PIPELINES_ENDPOINT)

def test_primary_type_oil_pipelines():
    check_primary_type(OIL_PIPELINES_ENDPOINT, 'pipelines')

def test_secondary_type_oil_pipelines():
    check_secondary_type(OIL_PIPELINES_ENDPOINT, 'oil')

def test_has_coordinates_oil_pipelines():
    check_has_coordinates(OIL_PIPELINES_ENDPOINT)

# Petroleum product pipelines tests

def test_status_code_petroleum_product_pipelines():
    check_status_code(PETROLEUM_PRODUCT_PIPELINES_ENDPOINT)

def test_verify_json_petroleum_product_pipelines():
    verify_json(PETROLEUM_PRODUCT_PIPELINES_ENDPOINT)

def test_primary_type_petroleum_product_pipelines():
    check_primary_type(PETROLEUM_PRODUCT_PIPELINES_ENDPOINT, 'pipelines')

def test_secondary_type_petroleum_product_pipelines():
    check_secondary_type(PETROLEUM_PRODUCT_PIPELINES_ENDPOINT, 'petroleum_product')

def test_has_coordinates_petroleum_product_pipelines():
    check_has_coordinates(PETROLEUM_PRODUCT_PIPELINES_ENDPOINT)

# Oil refineries tests

def test_status_code_oil_refineries():
    check_status_code(OIL_REFINERIES_ENDPOINT)

def test_verify_json_oil_refineries():
    verify_json(OIL_REFINERIES_ENDPOINT)

def test_primary_type_oil_refineries():
    check_primary_type(OIL_REFINERIES_ENDPOINT, 'refineries')

def test_secondary_type_oil_refineries():
    check_secondary_type(OIL_REFINERIES_ENDPOINT, 'petroleum')

def test_has_coordinates_oil_refineries():
    check_has_coordinates(OIL_REFINERIES_ENDPOINT)

# Gas processing tests

def test_status_code_gas_processing():
    check_status_code(GAS_PROCESSING_ENDPOINT)

def test_verify_json_gas_processing():
    verify_json(GAS_PROCESSING_ENDPOINT)

def test_primary_type_gas_processing():
    check_primary_type(GAS_PROCESSING_ENDPOINT, 'processing')

def test_secondary_type_gas_processing():
    check_secondary_type(GAS_PROCESSING_ENDPOINT, 'gas')

def test_has_coordinates_gas_processing():
    check_has_coordinates(GAS_PROCESSING_ENDPOINT)

# Coal plant tests

def test_status_code_coal_plants():
    check_status_code(COAL_PLANTS_ENDPOINT)

def test_verify_json_coal_plants():
    verify_json(COAL_PLANTS_ENDPOINT)

def test_primary_type_coal_plants():
    check_primary_type(COAL_PLANTS_ENDPOINT, 'power_plants')

def test_secondary_type_coal_plants():
    check_secondary_type(COAL_PLANTS_ENDPOINT, 'coal')

def test_has_coordinates_coal_plants():
    check_has_coordinates(COAL_PLANTS_ENDPOINT)

# Natural gas plant tests

def test_status_code_natural_gas_plants():
    check_status_code(NATURAL_GAS_PLANTS_ENDPOINT)

def test_verify_json_natural_gas_plants():
    verify_json(NATURAL_GAS_PLANTS_ENDPOINT)

def test_primary_type_natural_gas_plants():
    check_primary_type(NATURAL_GAS_PLANTS_ENDPOINT, 'power_plants')

def test_secondary_type_natural_gas_plants():
    check_secondary_type(NATURAL_GAS_PLANTS_ENDPOINT, 'natural_gas')

def test_has_coordinates_natural_gas_plants():
    check_has_coordinates(NATURAL_GAS_PLANTS_ENDPOINT)

# Petroleum plant tests

def test_status_code_petroleum_plants():
    check_status_code(PETROLEUM_PLANTS_ENDPOINT)

def test_verify_json_petroleum_plants():
    verify_json(PETROLEUM_PLANTS_ENDPOINT)

def test_primary_type_petroleum_plants():
    check_primary_type(PETROLEUM_PLANTS_ENDPOINT, 'power_plants')

def test_secondary_type_petroleum_plants():
    check_secondary_type(PETROLEUM_PLANTS_ENDPOINT, 'petroleum')

def test_has_coordinates_petroleum_plants():
    check_has_coordinates(PETROLEUM_PLANTS_ENDPOINT)

# Nuclear plant tests

def test_status_code_nuclear_plants():
    check_status_code(NUCLEAR_PLANTS_ENDPOINT)

def test_verify_json_nuclear_plants():
    verify_json(NUCLEAR_PLANTS_ENDPOINT)

def test_primary_type_nuclear_plants():
    check_primary_type(NUCLEAR_PLANTS_ENDPOINT, 'power_plants')

def test_secondary_type_nuclear_plants():
    check_secondary_type(NUCLEAR_PLANTS_ENDPOINT, 'nuclear')

def test_has_coordinates_nuclear_plants():
    check_has_coordinates(NUCLEAR_PLANTS_ENDPOINT)

# Hydroelectric plant tests

def test_status_code_hydroelectric_plants():
    check_status_code(HYDROELECTRIC_PLANTS_ENDPOINT)

def test_verify_json_hydroelectric_plants():
    verify_json(HYDROELECTRIC_PLANTS_ENDPOINT)

def test_primary_type_hydroelectric_plants():
    check_primary_type(HYDROELECTRIC_PLANTS_ENDPOINT, 'power_plants')

def test_secondary_type_hydroelectric_plants():
    check_secondary_type(HYDROELECTRIC_PLANTS_ENDPOINT, 'hydroelectric')

def test_has_coordinates_hydroelectric_plants():
    check_has_coordinates(HYDROELECTRIC_PLANTS_ENDPOINT)

# Wind farms/wind plant tests

def test_status_code_wind_plants():
    check_status_code(WIND_PLANTS_ENDPOINT)

def test_verify_json_wind_plants():
    verify_json(WIND_PLANTS_ENDPOINT)

def test_primary_type_wind_plants():
    check_primary_type(WIND_PLANTS_ENDPOINT, 'power_plants')

def test_secondary_type_wind_plants():
    check_secondary_type(WIND_PLANTS_ENDPOINT, 'wind')

def test_has_coordinates_wind_plants():
    check_has_coordinates(WIND_PLANTS_ENDPOINT)

# Solar plant tests

def test_status_code_solar_plants():
    check_status_code(SOLAR_PLANTS_ENDPOINT)

def test_verify_json_solar_plants():
    verify_json(SOLAR_PLANTS_ENDPOINT)

def test_primary_type_solar_plants():
    check_primary_type(SOLAR_PLANTS_ENDPOINT, 'power_plants')

def test_secondary_type_solar_plants():
    check_secondary_type(SOLAR_PLANTS_ENDPOINT, 'solar')

def test_has_coordinates_solar_plants():
    check_has_coordinates(SOLAR_PLANTS_ENDPOINT)

# Geothermal plant tests

def test_status_code_geothermal_plants():
    check_status_code(GEOTHERMAL_PLANTS_ENDPOINT)

def test_verify_json_geothermal_plants():
    verify_json(GEOTHERMAL_PLANTS_ENDPOINT)

def test_primary_type_geothermal_plants():
    check_primary_type(GEOTHERMAL_PLANTS_ENDPOINT, 'power_plants')

def test_secondary_type_geothermal_plants():
    check_secondary_type(GEOTHERMAL_PLANTS_ENDPOINT, 'geothermal')

def test_has_coordinates_geothermal_plants():
    check_has_coordinates(GEOTHERMAL_PLANTS_ENDPOINT)