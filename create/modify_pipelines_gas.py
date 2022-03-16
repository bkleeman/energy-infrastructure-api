try:
    import simplejson as json
except ImportError:
    import json


with open('../data/pipeline_data/NaturalGas_InterIntrastate_Pipelines_US_cleaned.json', 'r') as f:
    file_data = json.loads(f.read())

with open('../data/new_pipeline_data/gas_pipelines_cleaned.json', 'w') as f:
    for feature in file_data["features"]:
        feature["properties"] = { "original" : feature["properties"]}
        feature["properties"]["required"] = {
            "unit": "",
            # visual dimension
            "viz_dim": "",
            "legend": "Gas pipelines",
            "years": []
        }

        feature["properties"]["optional"] = {
            "description": "",
        }

        feature["properties"]["type"] = {
            "primary": "pipelines",
            "secondary": "gas"
        }

    json.dump(file_data, f)



