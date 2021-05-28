# import cloudconvert

# cloudconvert.configure(api_key = 'PPdfoduimgXcRtEBpQj0eubtFaWTIocOIwD1e3IJ4xah3BY8afut6W4x6KjpUyDL', sandbox = False)


import os
import re

#Used to convert Video to GIF.
from moviepy.editor import *

#this code converts GIF to webp
# from PIL import Image, ImageSequence
# from PIL import features
# print(features.check("webp_anim"))
# image_old = 'media/sample.jpeg'
# sequence = []
# im = Image.open(image_old)
# for frame in ImageSequence.Iterator(im):
#     sequence.append(frame.copy())
# # print(sequence)
# image_new = 'gif-test-3.webp'
# sequence[0].save(image_new, save_all=True,  append_images = sequence[1:])



# # this is used to convert video into gif
# from moviepy.editor import *
# import os
# clip = VideoFileClip("2886639388224.mp4")
# # clip = clip.subclip(0, 3)
# print(clip.fps)
# print(clip.duration)
# print(clip.fps*clip.duration)
# clip.write_gif("mygif-10.gif",fps=10)
# clip.write_gif("mygif.gif")

def VidToGif(filepath,trueform=False):
    flag = 0
    try:
        clip = VideoFileClip(filepath)
        length = clip.duration
        fps = clip.fps
        file_info = f"\n[FILE_INFO]:Length:{length} FPS:{fps} Total Frames:{length*fps}"
        if length <=10:
            if trueform or fps<10:
                clip.write_gif("media/temp-gif/outGIF_true.gif")
                flag = 1
            else:
                clip.write_gif("media/temp-gif/outGIF.gif",fps=10)
                flag = 1
                        
            if os.path.exists(filepath):
                os.remove(filepath)
            else:
                print("[ERROR] File does not exist at: " + filepath)

            print("File converted successfully")
            print(file_info)
            return(True)
        else:
            print("Video lenght has exceeded limit of 5 min.")
            print(file_info)
            return(False)

    except Exception as e:
        print(f"[Error Occured]:{e}")
        print(file_info)
        if flag == 1:
            print("Still File Converted Succecfully..")
            return(True)
        return(False)


mfc = "2289456545648.mp4"
VidToGif(f"media/{mfc}")





