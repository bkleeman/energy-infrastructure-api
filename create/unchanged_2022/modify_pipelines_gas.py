try:
    import simplejson as json
except ImportError:
    import json


with open('../../data/unchanged_2022/original/NaturalGas_InterIntrastate_Pipelines_US.geojson', 'r') as f:
    file_data = json.loads(f.read())

with open('../../data/unchanged_2022/modified/NaturalGas_InterIntrastate_Pipelines_US.geojson', 'w') as f:
    for feature in file_data["features"]:
        feature["properties"] = { "original" : feature["properties"]}
        feature["properties"]["required"] = {
            "unit": "",
            # visual dimension
            "viz_dim": "",
            "legend": "Gas pipelines",
            "years": {
                "actual": 0,
                "nominal": 2022
            }
        }

        feature["properties"]["optional"] = {
            "description": "",
        }

        feature["properties"]["type"] = {
            "primary": "pipelines",
            "secondary": "gas"
        }

    json.dump(file_data, f)



