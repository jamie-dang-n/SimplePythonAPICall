import requests as re

url_host = "https://dog.ceo"
endpoint = "/api/breeds/list/all"

url = url_host + endpoint 

response = re.get(url)

print(response.json())