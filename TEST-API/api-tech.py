import requests
import json

api_key = "6kvLNN-ytyBHL-NBLnIz-J9zWD2-ORuPzN"
url = 'https://api.i-tech.id/anim/hentai?key=6kvLNN-ytyBHL-NBLnIz-J9zWD2-ORuPzN'

payload ={
    "key": api_key,
}

response = requests.get(url)
print(response)
print(response.content)
# resp = json.load(response.content)
# print(f"[SIMI]: {resp['atext']}")
