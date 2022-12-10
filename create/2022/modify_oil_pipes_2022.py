try:
    import simplejson as json
except ImportError:
    import json


with open('../../data/2022/original/CrudeOil_Pipelines_US_EIA.geojson', 'r') as f:
    file_data = json.loads(f.read())

with open('../../data/2022/modified/CrudeOil_Pipelines_US_EIA.geojson', 'w') as f:
    for feature in file_data["geometries"]:
        feature["properties"] = { "original" : ""}
        feature["properties"]["required"] = {
            "unit": None,
            # visual dimension
            "viz_dim": None,
            "legend": "Oil pipelines",
            "years": {
                "actual": 0,
                "nominal": 2022
            }
        }

        feature["properties"]["optional"] = {
            "description": "",
        }

        feature["properties"]["type"] = {
            "primary": "pipeline",
            "secondary": "oil"
        }

    json.dump(file_data, f)