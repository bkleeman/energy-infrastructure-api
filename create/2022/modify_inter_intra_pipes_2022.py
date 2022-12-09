try:
    import simplejson as json
except ImportError:
    import json


with open('../../data/2022/original/NaturalGas_InterIntrastate_Pipelines_US_EIA.json', 'r') as f:
    file_data = json.loads(f.read())

with open('../../data/2022/modified/NaturalGas_InterIntrastate_Pipelines_US_EIA.json', 'w') as f:
    for feature in file_data["geometries"]:
        feature["properties"] = { "original" : ""}
        feature["properties"]["required"] = {
            "unit": None,
            # visual dimension
            "viz_dim": None,
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
            "primary": "pipeline",
            "secondary": "gas"
        }

    json.dump(file_data, f, indent=2)