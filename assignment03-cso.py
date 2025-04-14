# ------------------------------------------------------------------------
# Assignment 03
# ------------------------------------------------------------------------
# Author: Carlos Rigueti
# ------------------------------------------------------------------------

import json
import requests

# Fetch the Exchequer Account dataset from CSO
api_endpoint = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"
res = requests.get(api_endpoint)

# Save the retrieved JSON data to a file
if res.ok:
    with open("cso_data.json", "w") as output:
        json.dump(res.json(), output, indent=2)
