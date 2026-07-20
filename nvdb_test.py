import json

with open("/Users/arjumanbanu/Desktop/QGIS/Stavanger_Kommune/Bergen/response_1784412846986.json", "r") as f:

    data = json.load (f)
    
    print("Keys:", data.keys())
    print("Number of objects:", len(data["objekter"]))
8



    
