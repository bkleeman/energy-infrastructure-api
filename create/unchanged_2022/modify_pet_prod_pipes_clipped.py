try:
    import simplejson as json
except ImportError:
    import json

with open('../../data/unchanged_2022/original/PetroleumProduct_Pipelines_US_Nov2014_clipped.geojson', 'r') as f:
    file_data = json.loads(f.read())

with open('../../data/unchanged_2022/modified/PetroleumProduct_Pipelines_US_Nov2014_clipped.geojson', 'w') as f:
    for feature in file_data["features"]:
        feature["properties"]["required"] = {
            "unit": None,
            # visual dimension
            "viz_dim": None,
            "legend": "Petroleum product pipelines",
            "years": {
                "actual": 0,
                "nominal": 2022
            }
        }

    json.dump(file_data, f)