import json

with open("/Users/arjumanbanu/Desktop/QGIS/Stavanger_Kommune/Bergen/response_1784412846986.json", "r") as f:

    data = json.load (f)
    
print(data["objekter"][0].keys())