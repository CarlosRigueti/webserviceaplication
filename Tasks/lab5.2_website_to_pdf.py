#  A script that will convert the Wikipedia website into a pdf.

import requests
import urllib.parse
from config import apikeys as cfg

target_url = "https://en.wikipedia.org"

apiKey = cfg["htmltopdfkey"]  # Fetch the API key from the config
api_url = "https://api.html2pdf.app/v1/generate"

params = {'html': target_url, 'apiKey': apiKey}  # Correct usage of apiKey
parsedparams = urllib.parse.urlencode(params)

requestUrl = api_url + "?" + parsedparams

print(requestUrl)
response = requests.get(requestUrl)

print(response.status_code)

result = response.content

with open("document.pdf", "wb") as handler:
    handler.write(result)
    print("File saved")
