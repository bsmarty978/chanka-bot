import requests
import json

# url = 'api.giphy.com/v1/gifs/search'
# url = 'https://api.giphy.com/v1/stickers/search?api_key=KmOL7HpQnzgDciiPqYxPLofhkzSnpYtf&q=jujutsu'
# payload ={
#     "api_key": api_key,
#     "q": "superman"
# }

# response = requests.get(url)
# print(response)
# print(response.content)

api_key = "KmOL7HpQnzgDciiPqYxPLofhkzSnpYtf"
query = 'boobs'
surl = f'https://api.giphy.com/v1/stickers/search?api_key={api_key}&q={query}&limit=1'
gurl = f'https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={query}&limit=5&random_id=e826c9fc5c929e0d6c6d423841a282aa'

rgurl = f'api.giphy.com/v1/gifs/random?api_key={api_key}&tag={query}'

random_id = f'api.giphy.com/v1/randomid?api_key={api_key}'

response = requests.get(random_id)
# data = response.json()['data']
# for d in data:
#     print(d['url'])


