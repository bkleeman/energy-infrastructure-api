try:
    import simplejson as json
except ImportError:
    import json


with open('../../data/unchanged_2022/original/grid-100_300.json', 'r') as f:
    file_data = json.loads(f.read())

with open('../../data/unchanged_2022/modified/grid-100_300.json', 'w') as f:
    for feature in file_data["features"]:
        feature["properties"] = { "original" : feature["properties"]}
        feature["properties"]["required"] = {
            "unit": "kV",
            # visual dimension
            "viz_dim": "class",
            "legend": "AC 100-300 kV",
            "years": {
                "actual": 0,
                "nominal": 2022
            }
        }

        feature["properties"]["optional"] = {
            "description": "",
        }

        feature["properties"]["type"] = {
            "primary": "electric_grid",
            "secondary": "100_300_kV_AC"
        }

    json.dump(file_data, f)