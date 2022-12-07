try:
    import simplejson as json
except ImportError:
    import json


with open('./data/Petroleum_Refineries_US_2015.geojson', 'r') as f:
    file_data = json.loads(f.read())

with open('./data/new_refinery_data/Petroleum_Refineries_US_2015.geojson', 'w') as f:
    for feature in file_data["features"]:
        # feature["geometry"] = {
        #     "type": "Point",
        #     "coordinates": [feature["properties"]["coordinates"], feature["properties"]["coordinates"]]
        # }

        feature["properties"] = { "original" : feature["properties"]}

        feature["properties"]["required"] = {
        "unit": None,
        # visual dimension
        "viz_dim": None,
        "legend": "Oil refineries",
        "years": []
    }

        feature["properties"]["optional"] = {
            "description": "",
        }

        feature["properties"]["type"] = {
            "primary": "refineries",
            "secondary": "petroleum",
        }

        
    json.dump(file_data, f)