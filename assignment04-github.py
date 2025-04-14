# Assignment 04 – GitHub File Edit Script
# Author: Carlos Rigueti

import requests
import re
from github import Github
from config import config as cfg

# Load GitHub access token from config
token = cfg["privatekey"]  # Make sure this matches your config.py key

# Authenticate with GitHub
g = Github(token)

# Access the target GitHub repository
repo = g.get_repo("CarlosRigueti/aprivateone")

# Fetch the file from the repository
file_info = repo.get_contents("wikipedia.txt")
file_url = file_info.download_url

# Download the file content
response = requests.get(file_url)
original_text = response.text

# Replace "Andrew" with "Carlos"
updated_text = re.sub(r"\bAndrew\b", "Carlos", original_text, flags=re.IGNORECASE)

# Commit updated file back to GitHub
commit_msg = "Updated 'Andrew' to 'Carlos' using Python script"
update_response = repo.update_file(file_info.path, commit_msg, updated_text, file_info.sha)

print("✅ File updated successfully!")
