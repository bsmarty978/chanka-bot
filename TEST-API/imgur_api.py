
# import webbrowser
# from imgur_python import Imgur

# imgur_client = Imgur({'client_id': '7cfcd8b4bb350c3'})
# auth_url = imgur_client.authorize()
# webbrowser.open(auth_url)

from imgur_python import Imgur

imgur_client = Imgur({'client_id': '7cfcd8b4bb350c3'})
access_token = imgur_client.access_token()
print(access_token)