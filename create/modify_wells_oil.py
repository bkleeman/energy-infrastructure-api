try:
    import simplejson as json
except ImportError:
    import json


with open('../data/wells_oil.json', 'r') as f:
    file_data = json.loads(f.read())

with open('../data/well_data/wells_oil.json', 'w') as f:
    for feature in file_data["features"]:
        if feature["properties"]["lon"] is None:
            with open('../data/logfile.txt', 'a') as lf:
                lf.write('skipped file:' + str(feature))
            continue
        feature["geometry"] = {
            "type": "Point",
            "coordinates": [feature["properties"]["lon"], feature["properties"]["lat"]]
        }

        feature["properties"] = { "original" : feature["properties"]}
        feature["properties"]["required"] = {
        "unit": None,
        # visual dimension
        "viz_dim": "zoom",
        "legend": "Oil wells",
        "years": []
    }

        feature["properties"]["optional"] = {
            "description": "",
        }

        feature["properties"]["type"] = {
            "primary": "wells",
            "secondary": "oil"
        }

    json.dump(file_data, f)