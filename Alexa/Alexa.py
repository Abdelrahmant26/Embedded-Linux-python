import speech_recognition as sr
import os
import time
import subprocess
def question(order):
    if order[0] == "what":
        if "time" in order:
            timee=subprocess.check_output("date +%R",shell=True)
            print(timee)
            os.system(f"{prefix}\"time is {timee.decode()}\"")
        elif "date" in order:
            datee=subprocess.check_output("date +\"%A %d %B\"",shell=True)
            print(datee)
            os.system(f"{prefix}\"date is {datee.decode()}\"")
        elif "year" in order:
            datee=subprocess.check_output("date +%Y",shell=True)
            print(datee)
            os.system(f"{prefix}\"we are in {datee.decode()}\"")
        elif "day" in order:
            datee=subprocess.check_output("date +%A",shell=True)
            print(datee)
            os.system(f"{prefix}\"today is {datee.decode()}\"")
        elif "month" in order:
            datee=subprocess.check_output("date +%B",shell=True)
            print(datee)
            os.system(f"{prefix}\"we are in {datee.decode()}\"")
def obey(order):
    #execute/open :
    order=order.split()
    print(order[0])
    if order[0]=="open" or order[0]=="execute":
        print(order[1])
        os.system(order[1].lower())
    if order[0].lower() in ["what", "where", "who", "how", "when", "why"]:
        question(order)
r=sr.Recognizer()
prefix="spd-say -t female1 -r -30 -p 15 "
os.system(f"{prefix}\"Greetings, How are u today?\"")
time.sleep(3)
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    txt=r.recognize_google(audio)
    print(txt)
    os.system(f"{prefix}\"Google Speech Recognition thinks you said " + txt +"\"")
    os.system(f"{prefix}\"Sure\"")
    obey(txt)
except sr.UnknownValueError:
    os.system(f"{prefix}\"Google Speech Recognition could not understand audio\"")
except sr.RequestError as e:
    os.system(f"{prefix}\"Could not request results from Google Speech Recognition service; {0}\"".format(e))
