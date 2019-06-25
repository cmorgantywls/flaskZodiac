#THANK YOU PYAZTRO THESE ARE GREAT.
#pip install fuzzywuzzy[speedup]
#pip install pyaztro

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pyaztro

#get horoscope from pyaztro, save as usable dictionary bc dict() did NOT WORK, send back
def getHoroscope(theSign):
    if theSign == "Garbage":
         dictHoroscope = {"current_date": "IDK!","compatibility": "other garbage", "lucky_time": "when you learn to type", "lucky_number": "13", "color": "gross", "date_range": "IDK", "mood": "garbage mood", "description": "Well, this is awkward, but it seems like you entered something so wrong that even our sensors couldn't detect what you meant. Did you enter a month as a number? Or just type or sign in instead of a date (why are you using this app)? Either way, you broke something, and we don't know how to fix it. So guess your day is pretty rough, friend!"}
    else:
        horoscope = pyaztro.Aztro(sign=theSign)
        dictHoroscope = {
            "current_date": horoscope.current_date, 
            "compatibility": horoscope.compatibility, 
            "lucky_time": horoscope.lucky_time,
         "lucky_number": horoscope.lucky_number, 
         "color": horoscope.color, 
         "date_range": horoscope.date_range,
         "mood": horoscope.mood, 
         "description": horoscope.description
        }
    return dictHoroscope

#check if month is a match
def closeEnough(userInput,target):
    matchRatio = fuzz.partial_ratio(userInput, target)
    if matchRatio>=85:
        return True
    else:
        return False

#take month, day, determine sign
def getSign(month,day):
    if(closeEnough(month.lower(),"january") and (int(day)>=20 and int(day)<=31)) or (closeEnough(month.lower(),"february") and int(day)<=18):
        return "aquarius"
    elif(closeEnough(month.lower(),"february") and (int(day)>=19 and int(day)<=29)) or (closeEnough(month.lower(),"march") and int(day)<=20):
        return "pisces"
    elif(closeEnough(month.lower(),"march") and (int(day)>=21 and int(day)<=31)) or (closeEnough(month.lower(),"april") and int(day)<=19):
        return "aries"
    elif(closeEnough(month.lower(),"april") and (int(day)>=20 and int(day)<=30)) or (closeEnough(month.lower(),"may") and int(day)<=20):
        return "taurus"
    elif(closeEnough(month.lower(),"may") and (int(day)>=21 and int(day)<=31)) or (closeEnough(month.lower(),"june") and int(day)<=20):
        return "gemini"
    elif(closeEnough(month.lower(),"june") and (int(day)>=21 and int(day)<=30)) or (closeEnough(month.lower(),"july") and int(day)<=22):
        return "cancer"
    elif(closeEnough(month.lower(),"july") and (int(day)>=23 and int(day)<=31)) or (closeEnough(month.lower(),"august") and int(day)<=22):
        return "leo"
    elif(closeEnough(month.lower(),"august") and (int(day)>=23 and int(day)<=31)) or (closeEnough(month.lower(),"september") and int(day)<=22):
        return "virgo"
    elif(closeEnough(month.lower(),"september") and (int(day)>=23 and int(day)<=30)) or (closeEnough(month.lower(),"october") and int(day)<=22):
        return "libra"
    elif(closeEnough(month.lower(),"october") and (int(day)>=23 and int(day)<=31)) or (closeEnough(month.lower(),"november") and int(day)<=21):
        return "scorpio"
    elif(closeEnough(month.lower(),"november") and (int(day)>=22 and int(day)<=30)) or (closeEnough(month.lower(),"december") and int(day)<=21):
        return "saggitarius"
    elif(closeEnough(month.lower(),"december") and (int(day)>=22 and int(day)<=31)) or (closeEnough(month.lower(),"january") and int(day)<=19):
        return "capricorn"
    else:
        return "Garbage"

def getMedia(sign):
    if sign=="Garbage":
        youtubeVid = "https://www.youtube.com/embed/FZUcpVmEHuk"
        logo = "static/zodiacImages/garbage.svg"
        poster = "static/zodiacImages/garbagePoster.gif"
    elif sign=="capricorn":
        youtubeVid = "https://www.youtube.com/embed/dT0It2ErsCg"
        logo = "static/zodiacImages/capricorn.png"
        poster = "static/zodiacImages/ainorweiLinCapricornPoster.png"
    elif sign=="saggitarius":
        youtubeVid = "https://www.youtube.com/embed/igEyGK7Fjlg"
        logo = "static/zodiacImages/saggitarius.png"
        poster = "static/zodiacImages/ainorweiLinSaggitariusPoster.png"
    elif sign=="scorpio":
        youtubeVid = "https://www.youtube.com/embed/sPMFN8WdQ-M"
        logo = "static/zodiacImages/scorpio.png"
        poster = "static/zodiacImages/ainorweiLinScorpioPoster.png"
    elif sign=="libra":
        youtubeVid = "https://www.youtube.com/embed/TkMNCgqNuwQ"
        logo = "static/zodiacImages/libra.png"
        poster = "static/zodiacImages/ainorweiLinLibraPoster.png"
    elif sign=="virgo":
        youtubeVid = "https://www.youtube.com/embed/zXIsFv5Zbyk"
        logo = "static/zodiacImages/virgo.png"
        poster = "static/zodiacImages/ainorweiLinVirgoPoster.png"
    elif sign=="leo":
        youtubeVid = "https://www.youtube.com/embed/JXkhqKXwUlA"
        logo = "static/zodiacImages/leo.png"
        poster = "static/zodiacImages/ainorweiLinLeoPoster.png"
    elif sign=="cancer":
        youtubeVid = "https://www.youtube.com/embed/nV-VsoQhdV4"
        logo = "static/zodiacImages/cancer.png"
        poster = "static/zodiacImages/ainorweiLinCancerPoster.png"
    elif sign=="gemini":
        youtubeVid = "https://www.youtube.com/embed/fvQd_9y97rw"
        logo = "static/zodiacImages/gemini.png"
        poster = "static/zodiacImages/ainorweiLinGeminiPoster.png"
    elif sign=="taurus":
        youtubeVid = "https://www.youtube.com/embed/IBpn-zxt7Y0"
        logo = "static/zodiacImages/taurus.png"
        poster = "static/zodiacImages/ainorweiLinTaurusPoster.png"
    elif sign=="aries":
        youtubeVid = "https://www.youtube.com/embed/oS4OShiC0EY"
        logo = "static/zodiacImages/aries.png"
        poster = "static/zodiacImages/ainorweiLinAriesPoster.png"
    elif sign=="pisces":
        youtubeVid = "https://www.youtube.com/embed/1OICPHJ4Ovw"
        logo = "static/zodiacImages/pisces.png"
        poster = "static/zodiacImages/ainorweiLinPiscesPoster.png"
    elif sign=="aquarius":
        youtubeVid = "https://www.youtube.com/embed/fuA6rS6DTmk"
        logo = "static/zodiacImages/aquarius.png"
        poster = "static/zodiacImages/ainorweiLinAquariusPoster.png"
    mediaDict={"youtubeVid":youtubeVid,"logo":logo,"poster":poster}
    return mediaDict

