try:
    import simplejson as json
except ImportError:
    import json


with open('./data/grid-unk_under_100.json', 'r') as f:
    file_data = json.loads(f.read())

with open('./data/new_data/grid-unk_under_100.json', 'w') as f:
    for feature in file_data["features"]:
        feature["properties"] = { "original" : feature["properties"]}
        feature["properties"]["required"] = {
            "unit": "kV",
            # visual dimension
            "viz_dim": "class",
            "legend": "AC < 100 kV",
            "years": []
        }

        feature["properties"]["optional"] = {
            "description": "",
        }

        feature["properties"]["type"] = {
            "primary": "electric_grid",
            "secondary": "under_100"
        }

    json.dump(file_data, f)