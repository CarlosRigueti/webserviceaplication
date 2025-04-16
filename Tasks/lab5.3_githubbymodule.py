from github import Github
from config2 import config as cfg  # Ensure config2 is the correct file name
import requests

apikey = cfg["htmltopdfkey"]
g = Github(apikey)

repo = g.get_repo("CarlosRigueti/aprivateone")
file_info = repo.get_contents("test.txt")
url_of_file = file_info.download_url

response = requests.get(url_of_file)
content_of_file = response.text

new_contents = content_of_file + "\n...more stuff"

git_hub_response = repo.update_file(file_info.path, "updated by prog", new_contents, file_info.sha)
print(git_hub_response)
