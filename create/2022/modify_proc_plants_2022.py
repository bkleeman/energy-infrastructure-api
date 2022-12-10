try:
    import simplejson as json
except ImportError:
    import json


with open('../../data/2022/original/Natural_Gas_Processing_Plants.json', 'r') as f:
    file_data = json.loads(f.read())

with open('../../data/2022/modified/Natural_Gas_Processing_Plants.json', 'w') as f:
    for feature in file_data["features"]:
        feature["geometry"] = {
            "type": "Point",
            "coordinates": [feature["properties"]["LONGITUDE"], feature["properties"]["LATITUDE"]]
        }

        feature["properties"] = { "original" : feature["properties"]}
        feature["properties"]["required"] = {
            "unit": None,
            # visual dimension
            "viz_dim": "GASCAP",
            "legend": "Gas processing plants",
            "years": {
                "actual": 0,
                "nominal": 2022
            }
        }

        feature["properties"]["optional"] = {
            "description": "",
            "name": "gas_proc_plants"
        }

        feature["properties"]["type"] = {
            "primary": "processing_plant",
            "secondary": "gas"
        }

    json.dump(file_data, f)