import requests

url = "https://api.imgflip.com/get_memes"

response = requests.get(url)

print(response.text)