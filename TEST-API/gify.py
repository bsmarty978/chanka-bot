import requests
import json


api_key = "KmOL7HpQnzgDciiPqYxPLofhkzSnpYtf"
url = 'https://api.giphy.com/v1/stickers/search?api_key=KmOL7HpQnzgDciiPqYxPLofhkzSnpYtf&q=jujutsu&limit=1&offset=0&rating=g&lang=en'


payload ={
    "api_key": api_key,
    "q": "superman"
}

response = requests.get(url)
print(response)
print(response.content)