try:
    import simplejson as json
except ImportError:
    import json


with open('../../data/2022/original/Coal_Mines_2022.json', 'r') as f:
    file_data = json.loads(f.read())

with open('../../data/2022/modified/Coal_Mines_2022.json', 'w') as f:
    for feature in file_data["features"]:
        feature["geometry"] = {
            "type": "Point",
            "coordinates": [feature["properties"]["X"], feature["properties"]["Y"]]
        }
        
        feature["properties"] = { "original" : feature["properties"]}
        feature["properties"]["required"] = {
            "unit": "short tons",
            # visual dimension
            "viz_dim": "tot_prod", 
            "legend": "Coal mines",
            "years": {
                "actual": 2022,
                "nominal": 2022
            }
        }

        feature["properties"]["optional"] = {
            "description": "",
        }

        feature["properties"]["type"] = {
            "primary": "mine",
            "secondary": "coal"
        }

    json.dump(file_data, f)