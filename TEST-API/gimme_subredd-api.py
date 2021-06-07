import requests
import time
import asyncio
import aiohttp

now = time.time()
async def get(url, session,media_count):
    try:
        async with session.get(url=url) as response:
            resp = await response.read()
            print("Successfully got url {} with resp of length {}.".format(url, len(resp)))
            f = open(f"media/temp-sr/srm{media_count}.jpg","wb")
            f.write(resp)
            f.close()
    except Exception as e:
        print(f"Unable to get url {url} due to {e}.")


async def runner(urls):
    async with aiohttp.ClientSession() as session:
        ret = await asyncio.gather(*[get(url, session,media_count) for media_count,url in enumerate(urls)])
    print("Finalized all. Return is a list of len {} outputs.".format(len(ret)))


url= 'https://meme-api.herokuapp.com/gimme'
query = 'hentai'
count = 5
if query=='':
    pass_url = f"{url}/{count}"
else:
    pass_url = f"{url}/{query}/{count}"

print(pass_url)
resp = requests.get(pass_url)
print(resp.content)
if resp.status_code == 200:
    data = resp.json().get('memes')
    # media_count = 0
    url_list = []
    for d in data:
        url_list.append(d['preview'][-1])
    # print(url_list)
    i = 0
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    outter = asyncio.run(runner(url_list))
    counter = 0
    for d in data:
        post = d['postLink']
        sr = d['subreddit']
        title = d['title']
        orl = d['url']
        u = d['author']
        prl = d['preview'][-1]
        media_resp = f"media/temp-sr/srm{counter}.jpg"
        print("------------------------------")
        print(post)
        print(media_resp)
        print(prl)
        counter += 1

else:
    print("Error")

end = time.time()
print(f"time:{end-now}")


