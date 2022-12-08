try:
    import simplejson as json
except ImportError:
    import json


with open('../../data/2022/original/merged_refcap_eia_refineries.json', 'r') as f:
    file_data = json.loads(f.read())

with open('../../data/2022/modified/merged_refcap_eia_refineries.json', 'w') as f:
    for feature in file_data["features"]:
        feature["geometry"] = {
            "type": "Point",
            "coordinates": [feature["properties"]["X"], feature["properties"]["Y"]]
        }

        feature["properties"] = { "original" : feature["properties"]}

        feature["properties"]["required"] = {
        "unit": "Atmospheric Crude Distillation Capacity (barrels per stream day)",
        # visual dimension
        "viz_dim": 'QUANTITY',
        "legend": "Oil refineries",
        "years": {
            "actual": 0, "nominal": 2022
            }
    }

        feature["properties"]["optional"] = {
            "description": "",
        }

        feature["properties"]["type"] = {
            "primary": "refineries",
            "secondary": "petroleum",
        }

        
    json.dump(file_data, f)