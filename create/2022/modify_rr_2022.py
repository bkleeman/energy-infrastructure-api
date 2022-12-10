try:
    import simplejson as json
except ImportError:
    import json


with open('../../data/2022/original/Railroads_2022.json', 'r') as f:
    file_data = json.loads(f.read())

with open('../../data/2022/modified/Railroads_2022.geojson', 'w') as f:
    for feature in file_data["geometries"]:
        feature["properties"] = { "original" : ""}
        feature["properties"]["required"] = {
            "unit": None,
            # visual dimension
            "viz_dim": None,
            "legend": "Railroads",
            "years": {
                "nominal": 2022,
                "actual": 0
            }
        }

        feature["properties"]["optional"] = {
            "description": "",
        }

        feature["properties"]["type"] = {
            "primary": "railroads",
            "secondary": None
        }

    json.dump(file_data, f)