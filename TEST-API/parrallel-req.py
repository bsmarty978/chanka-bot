import time
import asyncio
import aiohttp
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
        ret = await asyncio.gather(*[get(url,session,media_count) for media_count,url in enumerate(urls)])

    print("Finalized all. Return is a list of len {} outputs.".format(len(ret)))
    


urls = ['https://preview.redd.it/b3tjngqjj4271.jpg?width=640&crop=smart&auto=webp&s=619ca506e0d794ab1468f88298d86682fc9a3bb2', 'https://preview.redd.it/mg70g935a6271.jpg?width=1080&crop=smart&auto=webp&s=fdd9a15bf10bdd71fdffe6491d866c03409f3257', 'https://preview.redd.it/ftiksqeve7271.jpg?width=960&crop=smart&auto=webp&s=ddd55993d2294ac5211fb38920a40c1def8e298e', 'https://preview.redd.it/2akxzryfo7271.jpg?width=640&crop=smart&auto=webp&s=2e665ff4912de9c87666f850d6f5ab51c276e337', 'https://external-preview.redd.it/PfQTeL7R2W-o_ADdWlxvwb5_OVyvFK6RA6tGUsUdZGQ.jpg?width=640&crop=smart&auto=webp&s=a7536b66c63f3008da0c235ee8991a1a9cb4e14a', 'https://preview.redd.it/gm52yr57c4271.jpg?width=640&crop=smart&auto=webp&s=af25970b40dc13548f151362de39b0e32dc351af', 'https://preview.redd.it/i59a7hceq5271.jpg?width=1080&crop=smart&auto=webp&s=6a0e4d4d067621bed8cc8ff308b10407ad91f502', 'https://preview.redd.it/nxim3l8wk7271.jpg?width=320&crop=smart&auto=webp&s=35ee3a0cbdd9d58c2b41f90958cb02d33bf000a6', 'https://preview.redd.it/tzjimvnft5271.jpg?width=1080&crop=smart&auto=webp&s=cc9deb41e23be8baeba2cc09f1990692fad537ee', 'https://preview.redd.it/q98dw3fna6271.jpg?width=1080&crop=smart&auto=webp&s=5902f7ca8e15961614f9f97d0910a1657a16c49e']
start = time.time()
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main(urls))
# loop.run_until_complete(asyncio.sleep(1))
# loop.close()

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
outter = asyncio.run(runner(urls))

end = time.time()

print("Took {} seconds to pull {} websites.".format(end - start, len(urls)))