try:
    import simplejson as json
except ImportError:
    import json

plant_codes = {
    "WAT": {
        "legend": "Hydroelectric power plants",
        "secondary_type": "hydroelectric"
    },
    "NG": {
        "legend": "Natural gas power plants",
        "secondary_type": "natural_gas"
    },
    "BIT": {
        "legend": "Coal power plants",
        "secondary_type": "coal"
    },
    "SUB": {
        "legend": "Coal power plants",
        "secondary_type": "coal"
    },
    "LIG": {
        "legend": "Coal power plants",
        "secondary_type": "coal"
    },
    "NUC": {
        "legend": "Nuclear power plants",
        "secondary_type": "nuclear"
    },
    "WND": {
        "legend": "Wind farms",
        "secondary_type": "wind"
    },
    "SUN": {
        "legend": "Solar PV",
        "secondary_type": "solar"
    },
    "GEO": {
        "legend": "Geothermal power plants",
        "secondary_type": "geothermal"
    },
    # Are all the biomass ones to be labeled as Biofuel in the legend and biomass as secondary_type?
    "AB": {
        "legend": "Biofuel",
        "secondary_type": "biomass"
    },
    "BLQ": {
        "legend": "Biofuel",
        "secondary_type": "biomass"
    },
    "LFG": {
        "legend": "Biofuel",
        "secondary_type": "biomass"
    },
    "MSW": {
        "legend": "Biofuel",
        "secondary_type": "biomass"
    },
    "OBG": {
        "legend": "Biofuel",
        "secondary_type": "biomass"
    },
    "OBL": {
        "legend": "Biofuel",
        "secondary_type": "biomass"
    },
    "OBS": {
        "legend": "Biofuel",
        "secondary_type": "biomass"
    },
    "TDF": {
        "legend": "Biofuel",
        "secondary_type": "biomass"
    },
    "WDL": {
        "legend": "Biofuel",
        "secondary_type": "biomass"
    },
    "WDS": {
        "legend": "Biofuel",
        "secondary_type": "biomass"
    },
    # Other fossil codes
    "BFG": {
        "legend": "Blast furnance gas power plants",
        "secondary_type": "other"
    },
    "DFO": {
        "legend": "Petroleum power plants",
        "secondary_type": "petroleum"
    },
    "JF": {
        "legend": "Petroleum power plants",
        "secondary_type": "petroleum"
    },
    "KER": {
        "legend": "Petroleum power plants",
        "secondary_type": "petroleum"
    },
    "OG": {
        "legend": "Petroleum power plants",
        "secondary_type": "petroleum"
    },
    "PC": {
        "legend": "Petroleum power plants",
        "secondary_type": "petroleum"
    },
    "PG": {
        "legend": "Petroleum power plants",
        "secondary_type": "petroleum"
    },
    "RC": {
        "legend": "Coal power plants",
        "secondary_type": "coal"
    },
    "RFO": {
        "legend": "Petroleum power plants",
        "secondary_type": "petroleum"
    },
    "SGC": {
        "legend": "Coal power plants",
        "secondary_type": "coal"
    },
    "SGP": {
        "legend": "Petroleum power plants",
        "secondary_type": "petroleum"
    },
    "WC": {
        "legend": "Coal power plants",
        "secondary_type": "coal"
    },
    "WO": {
        "legend": "Petroleum power plants",
        "secondary_type": "petroleum"
    },
    "MWH": {
        "legend": "Electricity used for energy storage",
        "secondary_type": "electricity_used_for_energy_storage"
    },
    "OTH": {
        "legend": "Other power plants",
        "secondary_type": "other"
    },
    "PUR": {
        "legend": "Purchased water steam power plants",
        "secondary_type": "purchased_water_steam"
    },
    "WH": {
        "legend": "Waste heat power plants",
        "secondary_type": "waste_heat"
    }
}

with open('../../data/2022/original/Power_Plants.json', 'r') as f:
    file_data = json.loads(f.read())

with open('../../data/2022/modified/Power_Plants.json', 'w') as f:
    for feature in file_data["features"]:
        feature["geometry"] = {
            "type": "Point",
            "coordinates": [feature["properties"]["LONGITUDE"], feature["properties"]["LATITUDE"]]
        }


        feature["properties"] = { "original" : feature["properties"]}
        feature["properties"]["required"] = {
            "unit": None,
            # visual dimension
            "viz_dim": "SUMMER_CAP",
            # "legend": feature["properties"]["original"]["PrimaryFue"] + " power plants",
            "years": {
                "actual": 0,
                "nominal": 2022
            }
        }

        feature["properties"]["optional"] = {
            "description": ""
        }

        feature["properties"]["type"] = {
            "primary": "power_plants",
            # "secondary": feature["properties"]["original"]["PrimaryFue"].lower()
        }

        for key in plant_codes:
            if feature["properties"]["original"]["PRIM_FUEL"] == key:
                feature["properties"]["required"]["legend"] = plant_codes[key]["legend"]
                feature["properties"]["type"]["secondary"] = plant_codes[key]["secondary_type"]

        # if feature["properties"]["original"]["PRIM_FUEL"] == "WAT":
        #     feature["properties"]["required"]["legend"] = plant_codes["WAT"]["legend"]
        #     feature["properties"]["type"]["secondary"] = plant_codes["WAT"]["secondary_type"]

    json.dump(file_data, f, indent=2)