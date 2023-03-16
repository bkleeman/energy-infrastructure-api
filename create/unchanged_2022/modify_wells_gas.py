try:
    import simplejson as json
except ImportError:
    import json


with open('../../data/unchanged_2022/original/wells_gas.json', 'r') as f:
    file_data = json.loads(f.read())

with open('../../data/unchanged_2022/modified/wells_gas.json', 'w') as f:
    for feature in file_data["features"]:
        feature["geometry"] = {
            "type": "Point",
            "coordinates": [feature["properties"]["lon"], feature["properties"]["lat"]]
        }

        feature["properties"] = { "original" : feature["properties"]}
        if feature["properties"]["original"]["class"] == "Off":
            feature["properties"]["required"] = {
            "unit": None,
            # visual dimension
            "viz_dim": "class",
            "legend": "Gas offshore wells",
            "years": {
                "actual": 0,
                "nominal": 2022
            }
        }

            feature["properties"]["optional"] = {
                "description": "",
            }

            feature["properties"]["type"] = {
                "primary": "wells",
                "secondary": "gas",
                "tertiary": "offshore"
            }

        else:
            feature["properties"]["required"] = {
                "unit": None,
                # visual dimension
                "viz_dim": "class",
                "legend": "Gas wells",
                "years": {
                    "actual": 0,
                    "nominal": 2022
                }
            }

            feature["properties"]["optional"] = {
                "description": "",
            }

            feature["properties"]["type"] = {
                "primary": "wells",
                "secondary": "gas"
            }

    json.dump(file_data, f)