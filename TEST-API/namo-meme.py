import requests
import json
url = "https://namo-memes.herokuapp.com/memes/20"

response = requests.get(url)

data = json.loads(response.text)

for d in data:
    print(d['url'])
    try:
        if (d['url']).endswith('gif'):
            resp = requests.get(d['url'])
            if resp.status_code == 200:
                f  = open("media/sample.gif","wb")
                f.write(resp.content)
                f.close()
            else:
                print("ing has been taken down by MODIJI")
        elif (d['url']).endswith('jpg'):
            resp = requests.get(d['url'])
            if resp.status_code == 200:
                f  = open("media/sample.jpg","wb")
                f.write(resp.content)
                f.close()
            else:
                print("ing has been taken down by MODIJI")
        elif (d['url']).endswith('jpeg'):
            resp = requests.get(d['url'])
            if resp.status_code == 200:
                f  = open("media/sample.jpeg","wb")
                f.write(resp.content)
                f.close()
            else:
                print("ing has been taken down by MODIJI")
        elif (d['url']).endswith('png'):
            resp = requests.get(d['url'])
            if resp.status_code == 200:
                f  = open("media/sample.png","wb")
                f.write(resp.content)
                f.close()
            else:
                print("ing has been taken down by MODIJI")
        else:
            print("Image has been taken down by MODIJI")
    except Exception as e:
        print(e)
        print("Image has been taken down by MODIJI")