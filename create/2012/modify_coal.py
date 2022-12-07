try:
    import simplejson as json
except ImportError:
    import json


with open('./data/coal_data/CoalMines_US_2013.geojson', 'r') as f:
    file_data = json.loads(f.read())

with open('./data/new_coal_data/CoalMines_US_2013.geojson', 'w') as f:
    for feature in file_data["features"]:

        feature["properties"] = { "original" : feature["properties"]}

        feature["properties"]["required"] = {
        "unit": "tot_prod",
        # visual dimension
        "viz_dim": "tot_prod",
        "legend": "Coal mines",
        "years": []
    }

        feature["properties"]["optional"] = {
            "description": "",
        }

        feature["properties"]["type"] = {
            "primary": "mines",
            "secondary": "coal",
        }

        
        json.dump(file_data, f, indent=4)