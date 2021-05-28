import requests
import json
url = "https://namo-memes.herokuapp.com/memes/10"

response = requests.get(url)

data = json.loads(response.text)
bad = 0
for d in data:
    print(d['url'])
    is_url_valid = True

    if (d['url']).endswith('gif'):
        media_url = d['url']
        extension = ".gif"
    elif (d['url']).endswith('jpg'):
        media_url = d['url']
        extension = ".jpg"
    elif (d['url']).endswith('jpeg'):
        media_url = d['url']
        extension = ".jpeg"
    elif (d['url']).endswith('png'):
        media_url = d['url']
        extension = ".png"
    else:
        is_url_valid = False
        bad += 1
    
    if is_url_valid:
        resp = requests.get(media_url)
        if resp.status_code == 200:
            try:
                f = open(f"media/samp{extension}","wb")
                f.write(resp.content)
                f.close()
            except Exception as e:
                print(f"Error:{e}")
                bad +=1
        else:
            bad += 1
if bad>0:
    print(f"{bad} bad urls")

    # try:
    #     if (d['url']).endswith('gif'):
    #         resp = requests.get(d['url'])
    #         if resp.status_code == 200:
    #             f  = open("media/sample.gif","wb")
    #             f.write(resp.content)
    #             f.close()
    #         else:
    #             print("ing has been taken down by MODIJI")
    #     elif (d['url']).endswith('jpg'):
    #         resp = requests.get(d['url'])
    #         if resp.status_code == 200:
    #             f  = open("media/sample.jpg","wb")
    #             f.write(resp.content)
    #             f.close()
    #         else:
    #             print("ing has been taken down by MODIJI")
    #     elif (d['url']).endswith('jpeg'):
    #         resp = requests.get(d['url'])
    #         if resp.status_code == 200:
    #             f  = open("media/sample.jpeg","wb")
    #             f.write(resp.content)
    #             f.close()
    #         else:
    #             print("ing has been taken down by MODIJI")
    #     elif (d['url']).endswith('png'):
    #         resp = requests.get(d['url'])
    #         if resp.status_code == 200:
    #             f  = open("media/sample.png","wb")
    #             f.write(resp.content)
    #             f.close()
    #         else:
    #             print("ing has been taken down by MODIJI")
    #     else:
    #         print("Image has been taken down by MODIJI")
    # except Exception as e:
    #     print(e)
    #     print("Image has been taken down by MODIJI")