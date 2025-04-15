import requests
import json

# Define the URL before using it
url = 'https://api.github.com/users/CarlosRigueti/repos?per_page=100'  # Example URL
# If you want to use a different URL, just replace it accordingly
# url = 'https://api.github.com/repos/CarlosRigueti/webserviceaplication/'

# Make the GET request
response = requests.get(url)

# Print the status code to see if the request was successful
print(response.status_code)

# Parse the JSON data from the response
repoJSON = response.json()

# You can print the JSON data or save it to a file
# For now, let's print it
print(json.dumps(repoJSON, indent=4))  # Pretty print the JSON data

# If you want to save the data to a file:
filename = "repos-private.json"
with open(filename, 'w') as f:
    json.dump(repoJSON, f, indent=4)