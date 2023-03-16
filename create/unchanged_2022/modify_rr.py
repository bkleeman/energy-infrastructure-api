try:
    import simplejson as json
except ImportError:
    import json


with open('../../data/unchanged_2022/original/railrdl020.geojson', 'r') as f:
    file_data = json.loads(f.read())

with open('../../data/unchanged_2022/modified/railrdl020.geojson', 'w') as f:
    for feature in file_data["features"]:
        feature["properties"] = { "original" : feature["properties"]}
        feature["properties"]["required"] = {
            "unit": None,
            # visual dimension
            "viz_dim": None,
            "legend": "Railroads",
            "years": {
                "actual": 0,
                "nominal": 2022
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