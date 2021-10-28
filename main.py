import requests as re

url_host = "https://dog.ceo"
endpoint = "/api/breeds/list/all"

url = url_host + endpoint 

response = re.get(url)
breeds = response.json()["message"]

# Get a list of all breeds from the API call
all_breeds = breeds.keys()

# Loop and print out each key
for breed in all_breeds:
  print(breed)

# Get a list of all subbreeds of a breed with at least 3 subbreeds
# But NOT bulldogs
# Examples include: poodles, retrievers, terriers, mastiffs, spaniels, setters, & more
terrier_subbreeds = breeds["terrier"]
input("\nPress enter to get all terrier subbreeds")
for sub in terrier_subbreeds:
  print(sub)

# Display all bulldog subbreeds
bulldog_subbreeds = breeds["bulldog"]
input("\nPress enter to get all bulldog subbreeds")
for sub in bulldog_subbreeds:
  print(sub)