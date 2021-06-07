import json
import random
import re
import requests
import time
import os

from moviepy.editor import *

from gtts import gTTS
import gtts

import asyncio
import aiohttp

import pymongo
import pandas as pd
import itertools
import dateparser as dp

#NOTE: fetches quotes from locak quote fil
#TO-DO: convert this method with API
with open("quotes.json","r") as f:
    d = f.read()
data = json.loads(d)

#NOTE: this is used get UserConfig data from UserConfig.json 
with open("UserConfig.json","r") as f:
    d = f.read()
config_data = json.loads(d)

help_msg = config_data.get("HELP_MSG")
prefix = config_data.get("PREFIX")

#NOTE: This is the class where every mods is store you can add you mods as function/method here accordingly...
#pass thr message object to every new mod
#NOTE:DON'T forget to add mod descrpition as comment to help other devs
class replymods:
    # def __init__(self,name="Chanka"):
    #     self.message = name

    def replyQuote(message):
        #sends random quotes
        quote = data[random.randint(0,1840)]["text"]
        message.reply_message(quote)

    def replyHelp(message):
        '''Sends help menu.'''
        message.reply_message(f"Lavde abhi kam chal rha he apna kam kr nalla gandu!!!!\n\n{help_msg}")
        
    def replyNoods(message):
        '''Sends random nudes.'''
        message.reply_message("Tharki sala porn dekh bathroom me jake<><>")

    def replyMenu(message):
        '''Sends menu.'''
        message.reply_message(help_msg)

    def replyModError(message):
        '''Sends Error msg with menu.'''
        message.reply_message(f"{message.content} bhosad ye mod nahi chal rha dusra try kr!!!\n\n{help_msg}")

    def replyNamo(message,driver,count=1):
        '''Sends random NAMO Memes.'''

        if count > 10:
            count = 10
        url = f"https://namo-memes.herokuapp.com/memes/{count}"

        response = requests.get(url)

        data = json.loads(response.text)

        bad = 0

        for d in data:
            print(d['url'])
            try:
                if (d['url']).endswith('gif'):
                    resp = requests.get(d['url'])
                    if resp.status_code == 200:
                        f  = open("media/sample.gif","wb")
                        f.write(resp.content)
                        f.close()
                        driver.send_media(path="media/sample.gif",chatid = message.chat_id, caption = "Pyare MODIJI")
                    else:
                        bad = bad + 1

                elif (d['url']).endswith('jpg'):
                    resp = requests.get(d['url'])
                    if resp.status_code == 200:
                        f  = open("media/sample.jpg","wb")
                        f.write(resp.content)
                        f.close()
                        driver.send_media(path="media/sample.jpg",chatid = message.chat_id, caption = "Pyare MODIJI")
                    else:
                        bad = bad + 1

                elif (d['url']).endswith('jpeg'):
                    resp = requests.get(d['url'])
                    if resp.status_code == 200:
                        f  = open("media/sample.jpeg","wb")
                        f.write(resp.content)
                        f.close()
                        driver.send_media(path="media/sample.jpeg",chatid = message.chat_id, caption = "Pyare MODIJI")
                    else:
                        bad = bad + 1

                elif (d['url']).endswith('png'):
                    resp = requests.get(d['url'])
                    if resp.status_code == 200:
                        f  = open("media/sample.png","wb")
                        f.write(resp.content)
                        f.close()
                        driver.send_media(path="media/sample.png",chatid = message.chat_id, caption = "Pyare MODIJI")
                    else:
                        bad = bad + 1

                else:
                    bad = bad + 1
            except Exception as e:
                print(e)
                bad = bad + 1
        if bad !=0:
            message.reply_message(f"{bad} images has been taken down by MODIJI")
    
    def replyPing(message):
        '''Sends Ping.'''
        current_time = time.ctime()
        hr = time.localtime().tm_hour

        if 5 <= hr <=11:
            ping_msg = f"Good Morning 🌅 🌇 🌄 Boiis\n No need to fear *LORD* is here.\n{current_time}\n\n LORD is doing workout with IQ, and you should also pump your body."
        elif 12 <= hr <= 17:
            ping_msg = f"Good afternoon 🌞 ⛅ 🕛 Boiss\n {current_time}\n\n *LORD* is doing some research with *MIRA* to upgrade his LMG."
        elif 18 <= hr <= 22:
            ping_msg = f"Good Evening 🌇 🌄 🌅 🌆 Boiss\n {current_time}\n\n *LORD* is in the evening traning session with *CAV*💀."
        else:
            ping_msg = f"Good Night 🌃 🌉 Boiis\n {current_time}\n\n *LORD* is going for bed 🛏 🛌 😴 💤 after having drink party 🍹 🍺 🎉 🥳  with his mates."
    

        message.reply_message(ping_msg)
    
    def replySticker(message,driver):
        '''Converts quoted media into webp and sends back as Sicther.'''
        main_msg = message
        try:
            quoted_msg = (message.get_js_obj())['quotedMsg']
            type = quoted_msg.get('type')
            print(type)
            if quoted_msg and type == 'image':
                q_msg_id = quoted_msg['id']
                print(q_msg_id)
                q_msg = driver.get_message_by_id(q_msg_id)
                print(f"q_msg:{q_msg}")
                if q_msg:
                    fname = q_msg.filename
                    print(fname)
                    q_msg.save_media("media/",force_download=True)
                    driver.send_image_as_sticker(path=f"media/{fname}",chatid = main_msg.chat_id)
                else:
                    main_msg.reply_message("Lord is busy so fuck off, come later!!!!")
            else:
                main_msg.reply_message("dumbass")
        except Exception as e:
            print(f"ERROR:{e}")
            main_msg.reply_message("Lord is busy so fuck off, come later.")

    # def replyVideoToGif(message,driver):
    #     '''Converts a video to a GIF and sends it back.'''
    #     def VidToGif(filepath,trueform=False):
    #         '''Converts a Video to GIF taking Video filepath return True Or False after Converting to GIF.''' 

    #         '''To get max quality GIF pass trueform = True.'''

    #         flag = 0
    #         try:
    #             clip = VideoFileClip(filepath)
    #             length = clip.duration
    #             fps = clip.fps
    #             file_info = f"\n[FILE_INFO]:Length:{length} FPS:{fps} Total Frames:{length*fps}"
    #             if length <=10:
    #                 if trueform or fps<10:
    #                     clip.write_gif("media/temp-gif/outGIF_true.gif")
    #                     flag = 1
    #                 else:
    #                     clip.write_gif("media/temp-gif/outGIF.gif",fps=10)
    #                     flag = 1
                                
    #                 if os.path.exists(filepath):
    #                     os.remove(filepath)
    #                 else:
    #                     print("[ERROR] File does not exist at: " + filepath)

    #                 print("File converted successfully")
    #                 print(file_info)
    #                 return(True)
    #             else:
    #                 print("Video lenght has exceeded limit of 5 min.")
    #                 print(file_info)
    #                 return(False)

    #         except Exception as e:
    #             print(f"[Error Occured]:{e}")
    #             print(file_info)
    #             if flag == 1:
    #                 print("Still File Converted Succecfully..")
    #                 return(True)
    #             return(False)

    #     try:
    #         quoted_msg = (message.get_js_obj())['quotedMsg'] #gets quoted msg DICt through JS-OBJ
    #         type = quoted_msg.get('type')                    #get type of message
    #         print(type)
    #         if quoted_msg and type == 'video':
    #             q_msg_id = quoted_msg['id']
    #             print(q_msg_id)
    #             q_msg = driver.get_message_by_id(q_msg_id)  #gets actual quoted message 
    #             print(f"q_msg:{q_msg}")
    #             if q_msg:
    #                 fname = q_msg.filename
    #                 print(fname)
    #                 q_msg.save_media("media/temp-gif/",force_download=True)
    #                 fpath = f"media/temp-gif/{fname}"
    #                 flag = VidToGif(fpath)
    #                 if flag:
    #                     driver.send_media(path="media/temp-gif/outGIF.gif",chatid = message.chat_id,caption = "gif by chevi")
    #                 else:
    #                     message.reply_message("Check limitaion suka blayat!!")
    #             else:
    #                 message.reply_message("Lord is busy so fuck off, come later!!!!")

    #     except Exception as e:
    #         print(f"[vidTOgid Error]:{e}")
    #         message.reply_message("Lord is busy right now.")

    def replyVideoToGif(message,driver):
        '''Converts a video to a GIF and sends it back.'''
        try:
            quoted_msg = (message.get_js_obj())['quotedMsg'] #gets quoted msg DICt through JS-OBJ
            type = quoted_msg.get('type')                    #get type of message
            print(type)
            if quoted_msg and type == 'video':
                q_msg_id = quoted_msg['id']
                print(q_msg_id)
                q_msg = driver.get_message_by_id(q_msg_id)  #gets actual quoted message 
                print(f"q_msg:{q_msg}")
                if q_msg:
                    fname = q_msg.filename
                    print(fname)
                    q_msg.save_media("media/temp-gif/",force_download=True)
                    fpath = f"media/temp-gif/{fname}"
                    if fname:
                        driver.send_video_as_gif(path=fpath,chatid = message.chat_id,caption = "gif by chevi")
                    else:
                        message.reply_message("Check limitaion suka blayat!!")
                else:
                    message.reply_message("Lord is busy so fuck off, come later!!!!")

        except Exception as e:
            print(f"[vidTOgif Error]:{e}")
            message.reply_message("Lord is busy right now.")

    
    def replySay(message,text,driver,lang = 'en'):
        '''Sends VOice message according to thr given text.'''
        try:
            # The text that you want to convert to audio
            mytext = text

            # Language in which you want to convert
            language = lang

            print(f"TExt:{mytext}\nLAng:{language}")

            if mytext:
                if language in gtts.lang.tts_langs():
                    # Passing the text and language to the engine,
                    # here we have marked slow=False. Which tells
                    # the module that the converted audio should
                    # have a high speed
                    myobj = gTTS(text=mytext, lang=language)

                    # Saving the converted audio in a mp3 file named
                    # media/temp-voice/outvoice.ogg
                    myobj.save("media/temp-voice/outvoice.mp3")
                    vmsg = driver.send_voice_note(path="media/temp-voice/outvoice.mp3",chatid = message.chat_id)
                    repmsg = driver.get_message_by_id(vmsg)
                    repmsg.reply_message(text)
                    # if vmsg:
                    #     os.remove("media/temp-voice/outvoice.mp3")
                    # else:
                    #     print("can not delete the file.")
                else:
                    message.reply_message("I can not speak that language.\n\nCheck the availabale languages by\n*$help say*")
            else:
                message.reply_message("Bhosdike command use krna sikkh..!!!\n\nUse this:\n*$say:I am noob*")
        except Exception as e:
            print(f"[Error while voice processing]:{e}")
            message.reply_message("Iq is busy right now she will be back after soon.")

    def replySr(message,driver,query="",count=1):
        if int(count) > 10:
            count = 10
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
            # print("Finalized all. Return is a list of len {} outputs.".format(len(ret)))


        url= 'https://meme-api.herokuapp.com/gimme'
        if query=='':
            pass_url = f"{url}/{count}"
        else:
            pass_url = f"{url}/{query}/{count}"

        resp = requests.get(pass_url)
        print(resp)
        if resp.status_code == 200:
            data = resp.json().get('memes')
            url_list = []
            for d in data:
                url_list.append(d['preview'][-1])
            
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
                cap= f"Title:{title}\nLink⛓: {post}\n r/{sr}\nu/{u} "
                driver.send_media(path=media_resp,chatid = message.chat_id, caption = cap)
                counter += 1

        else:
            message.reply_message("subreddit not found.")

    def replyRsixP(message,text,driver):
        client = pymongo.MongoClient("mongodb+srv://nameless_gambit:smtG886611@cluster0.zjdqc.mongodb.net/R6SDB?retryWrites=true&w=majority")
        db = client.dbr6s
        players = db.Players
        res = players.find({ '$text' : {'$search' : f'^.*{text}.*$'}})
        print(res.count())
        if res.count() == 1:
            result = res[0]
            ign  = result['ign']
            name = result['name']
            photo = result['photo']
            country = result['country']
            team = result['timeline'][-1]['teamname']
            statsdf = pd.DataFrame(res[0]['allstats'])
            statsdf.set_index('match_id',inplace=True)

            #TOTAL PARAMS:
            total_matches = result['total matches']
            total_kill = statsdf.kill.sum()
            total_death = statsdf.death.sum()
            total_e_kill = statsdf.entry_kill.sum()
            total_e_death = statsdf.entry_death.sum()
            total_cluth = statsdf['1vx'].sum()
            total_plant = statsdf.plant.sum()

            #AVERAGE PARAMS:
            avgs = statsdf.mean().round(2)

            #MAX PARAMS:
            maxs = statsdf.max()

            #BEST AND WROST PARAMS:
            best_r = statsdf.rating.max()
            worst_r = statsdf.rating.min()
            best = list(statsdf[statsdf.rating == statsdf.rating.max()].index)
            wrost = list(statsdf[statsdf.rating == statsdf.rating.min()].index)

            timeline = ""
            for t in result['timeline']:
                timeline = timeline+f"{t['teamname']} on {t['jointime'].strftime('%b %d %Y')}\n"

            cap_s = f"Ign:{ign}\nName:{name}\nCountry:{country}\nTeam:{team}\n\n"
            cap_total = f"Total Matches:{total_matches}\nTotal Kills:{total_kill}\nTotal Deaths:{total_death}\nTotal Entry Kills:{total_e_kill}\nTotal Entry Deaths:{total_e_death}\nTotal Clutches:{total_cluth}\nTotal Plant:{total_plant}\n\n"
            cap_avg = f"Average Stat:\n{avgs}\n\n"
            cap_max = f"Max stst:\n{maxs}\n\n"
            cap_bw = f"Best matches(Rating:{best_r}):{best}\nWrost Matches(Rating:{worst_r}):{wrost}\n\n"
            cap_time = f"Player Timeline:\n{timeline}"

            cap = cap_s+cap_total+cap_avg+cap_max+cap_bw+cap_time

            resp = requests.get(photo)
            if resp.status_code == 200:
                f  = open("media/temp-r6p/sample.jpg","wb")
                f.write(resp.content)
                f.close()
                driver.send_media(path="media/temp-r6p/sample.jpg",chatid = message.chat_id, caption = cap)
            else:
                driver.send_media(path="media/temp-r6p/defualt.jpg",chatid = message.chat_id, caption = cap)
        else:
            message.reply_message("Sorry! we can't find this player, check if PlayerName is correct.")   

    def replyRsixT(message,text,driver):
        client = pymongo.MongoClient("mongodb+srv://nameless_gambit:smtG886611@cluster0.zjdqc.mongodb.net/R6SDB?retryWrites=true&w=majority")
        db = client.dbr6s
        teams = db.Teams
        res = teams.find({ '$text' : {'$search' : f'^.*{text}.*$'}})
        print(res.count())
        if res.count()==1:
            result = res[0]
            name = result['name']
            country = result['country']
            flag = result['flag']
            total_matches = result['total matches']
            roster = result['roster']

            tdf = pd.DataFrame(result['allmatches'])

            win = int(tdf[tdf.result == "WON"].count().match_id)
            loss = int(tdf[tdf.result == "LOSS"].count().match_id)
            tie = int(tdf[tdf.result == "TIE"].count().match_id)

            explo = tdf.explode('roster').drop_duplicates(subset='roster')
            timeline = []
            for p,t in zip(list(explo.roster),list(explo.time)):
                timeline.append({
                    'time': t,
                    'player':p
                })

            rt=pd.DataFrame(timeline).groupby('time')['player'].apply(list)

            tline = ""
            for t,p in zip(rt.index,rt):
                tline = tline + f"{p} joined on {dp.parse(t).date()}\n"
            
            cap_s = f"Team Name:{name}\nCountry\Regoin:{country}\n\nCurrent Roster:{roster}\n\n"
            cap_st = f"Total Matches:{total_matches}\n\nWin/Loss(%):{win}/{loss}({round(win/loss,2)})\nTie:{tie}\n\n"
            cap_t = f"Roster Timeline:\n{tline}"

            cap = cap_s+cap_st+cap_t

            resp = requests.get(flag)
            if resp.status_code == 200:
                f  = open("media/temp-r6t/sample.jpg","wb")
                f.write(resp.content)
                f.close()
                driver.send_media(path="media/temp-r6t/sample.jpg",chatid = message.chat_id, caption = cap)
            else:
                driver.send_media(path="media/temp-r6t/defualt.jpg",chatid = message.chat_id, caption = cap)
        else:
            message.reply_message("Sorry! we can't find this Team, check if TeamName is correct.")
