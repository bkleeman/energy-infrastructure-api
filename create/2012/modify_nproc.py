try:
    import simplejson as json
except ImportError:
    import json


with open('./data/nproc.json', 'r') as f:
    file_data = json.loads(f.read())

with open('./data/new_data/nproc.json', 'w') as f:
    for feature in file_data["features"]:
        feature["geometry"] = {
            "type": "Point",
            "coordinates": [feature["properties"]["lat"], feature["properties"]["lon"]]
        }

        feature["properties"] = { "original" : feature["properties"]}

        feature["properties"]["required"] = {
        "unit": None,
        # visual dimension
        "viz_dim": None,
        "legend": "Gas processing",
        "years": []
    }

        feature["properties"]["optional"] = {
            "description": "",
        }

        feature["properties"]["type"] = {
            "primary": "processing",
            "secondary": "gas",
        }

        
    json.dump(file_data, f)