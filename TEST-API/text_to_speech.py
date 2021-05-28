# Import the required module for text
# to speech conversion


from gtts import gTTS
import gtts
from playsound import playsound
# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = 'mali gayi shanti?'

# Language in which you want to convert
language = 'ru'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language)

# Saving the converted audio in a mp3 file named
# welcome
rop = myobj.save("welcome.mp3")
print(f"roppop:{rop}")

# Playing the converted file
# os.system("mpg321 welcome.mp3")
playsound("welcome.mp3")

# all available languages along with their IETF tag
# print(gtts.lang.tts_langs())
# {'af': 'Afrikaans', 'ar': 'Arabic', 'bn': 'Bengali', 'bs': 'Bosnian', 'ca': 'Catalan', 'cs': 'Czech', 'cy': 'Welsh', 'da': 'Danish', 'de': 'German',
# 'el': 'Greek', 'en': 'English', 'eo': 'Esperanto', 'es': 'Spanish', 'et': 'Estonian', 'fi': 'Finnish', 'fr': 'French', 'gu': 'Gujarati',
# 'hi': 'Hindi', 'hr': 'Croatian', 'hu': 'Hungarian', 'hy': 'Armenian', 'id': 'Indonesian', 'is': 'Icelandic', 'it': 'Italian', 'ja': 'Japanese',
# 'jw': 'Javanese', 'km': 'Khmer', 'kn': 'Kannada', 'ko': 'Korean', 'la': 'Latin', 'lv': 'Latvian', 'mk': 'Macedonian', 'ml': 'Malayalam',
# 'mr': 'Marathi', 'my': 'Myanmar (Burmese)', 'ne': 'Nepali', 'nl': 'Dutch', 'no': 'Norwegian', 'pl': 'Polish', 'pt': 'Portuguese',
# 'ro': 'Romanian', 'ru': 'Russian', 'si': 'Sinhala', 'sk': 'Slovak', 'sq': 'Albanian', 'sr': 'Serbian', 'su': 'Sundanese', 'sv': 
# 'Swedish', 'sw': 'Swahili', 'ta': 'Tamil', 'te': 'Telugu', 'th': 'Thai', 'tl': 'Filipino', 'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu',
# 'vi': 'Vietnamese', 'zh-CN': 'Chinese', 'zh-TW': 'Chinese (Mandarin/Taiwan)', 'zh': 'Chinese (Mandarin)'}

###


#For Offline use

# import pyttsx3
# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()

# # pyttsx3.speak("I will speak this poem")
# text = "is it working?"
# engine.save_to_file(text, "python.ogg")
# engine.runAndWait()