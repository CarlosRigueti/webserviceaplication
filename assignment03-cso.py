# ------------------------------------------------------------------------
# Assignment 03
# ------------------------------------------------------------------------
# Author: Carlos Rigueti
# ------------------------------------------------------------------------

import requests, json

# Get data from CSO API
api_url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"
data = requests.get(api_url).json()

# Save to file
with open("cso.json", "w") as file:
    json.dump(data, file)

# Print the file name only
print("cso.json")
