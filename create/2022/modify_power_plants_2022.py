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
        "legend": "Lignite power plants",
        "secondary_type": "lignite"
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
    # Are all the biomass ones to be labeled as Biofuel in the legend and biodiesel as secondary_type?
    "AB": {
        "legend": "Biofuel",
        "secondary_type": "biodiesel"
    },
    "BLQ": {
        "legend": "Biofuel",
        "secondary_type": "biodiesel"
    },
    "LFG": {
        "legend": "Biofuel",
        "secondary_type": "biodiesel"
    },
    "MSW": {
        "legend": "Biofuel",
        "secondary_type": "biodiesel"
    },
    "OBG": {
        "legend": "Biofuel",
        "secondary_type": "biodiesel"
    },
    "OBL": {
        "legend": "Biofuel",
        "secondary_type": "biodiesel"
    },
    "OBS": {
        "legend": "Biofuel",
        "secondary_type": "biodiesel"
    },
    "TDF": {
        "legend": "Biofuel",
        "secondary_type": "biodiesel"
    },
    "WDL": {
        "legend": "Biofuel",
        "secondary_type": "biodiesel"
    },
    "WDS": {
        "legend": "Biofuel",
        "secondary_type": "biodiesel"
    },
    # Other fossil codes
    "BFG": {
        "legend": "Blast furnance gas power plants",
        "secondary_type": "blast_furnace_gas"
    },
    "DFO": {
        "legend": "Distillate fuel oil power plants",
        "secondary_type": "distillate_fuel_oil"
    },
    "JF": {
        "legend": "Jet fuel power plants",
        "secondary_type": "jet_fuel"
    },
    "KER": {
        "legend": "Kerosene power plants",
        "secondary_type": "kerosene"
    },
    "OG": {
        "legend": "Other gas power plants",
        "secondary_type": "other_gas"
    },
    "PC": {
        "legend": "Petroleum coke power plants",
        "secondary_type": "petroleum_coke"
    },
    "PG": {
        "legend": "Gaseous propane power plants",
        "secondary_type": "gaseous_propane"
    },
    "RC": {
        "legend": "Coal power plants",
        "secondary_type": "coal"
    },
    "RFO": {
        "legend": "Residual fuel oil power plants",
        "secondary_type": "residual_fuel_oil"
    },
    "SGC": {
        "legend": "Coal power plants",
        "secondary_type": "coal"
    },
    "SGP": {
        "legend": "Synthesis gas from petroleum coke power plants",
        "secondary_type": "synthesis_gas_from_petroleum_coke"
    },
    "WC": {
        "legend": "Coal power plants",
        "secondary_type": "coal"
    },
    "WO": {
        "legend": "Waste oil power plants",
        "secondary_type": "waste_oil"
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
            "coordinates": [feature["properties"]["X"], feature["properties"]["Y"]]
        }


        feature["properties"] = { "original" : feature["properties"]}
        feature["properties"]["required"] = {
            "unit": None,
            # visual dimension
            "viz_dim": "SUMMER_CAP",
            "legend": feature["properties"]["original"]["PrimaryFue"] + " power plants",
            "years": {
                "actual": 0,
                "nominal": 2022
            }
        }

        feature["properties"]["optional"] = {
            "description": ""
        }

        feature["properties"]["type"] = {
            "primary": "power_plant",
            "secondary": feature["properties"]["original"]["PrimaryFue"].lower()
        }



        if feature["properties"]["original"]["PRIM_FUEL"] == "WAT":
            # feature["properties"]["required"]["legend"]: "Hydroelectric power plants"
            # feature["properties"]["type"]["secondary"]: "hydroelectric"
            feature["properties"]["required"]["legend"] = plant_codes["WAT"]["legend"]
            feature["properties"]["type"]["secondary"] = plant_codes["WAT"]["secondary_type"]

    json.dump(file_data, f, indent=2)