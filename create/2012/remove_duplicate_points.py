# basic script to remove duplicate points from geojson coordinates
# a response to SO post at https://stackoverflow.com/questions/70071555/how-do-i-create-a-mongodb-2dsphere-index-on-a-document-containing-an-array-of-ar

try:
    import simplejson as json
except ImportError:
    import json

input = '../data/TightOil_ShaleGas_US_Aug2015.geojson'
output = '../data/new_data/TightOil_ShaleGas_US_Aug2015_no_duplicates.geojson'
with open(input, 'r') as f:
    file_data = json.loads(f.read())

with open(output, 'w') as f:
    for feature in file_data["features"]:
        coords = feature["geometry"]["coordinates"]
        if any(isinstance(i, list) for i in coords):
            for coord in coords:
                if any(isinstance(i, list) for i in coord):
                    for c in coord:
                        print('nested list')
        coords = [set(map(tuple, coord)) for coord in coords]
        
        # for coord in coords:
        #     list(dict.fromkeys(coord))
        # if any(isinstance(i, list) for i in coords):
        #     coords = set(map(tuple, coords))
        #     print(type(i))


        # for coord in coords[0]:
        #     coord = set(map(tuple, coord))
        # coords = set(tuple(coords))
        # coords = set(map(tuple, coords))
        # coords = set(map(tuple, coords[0]))
        # coords = set(tuple(coords))
        # try:
        #     coords = set(map(tuple, coords[0])) 
        # except:
        #     coords = set(map(tuple, coords))
        # coords = tuple(coords)
        print(type(coords))
        # print(coords)