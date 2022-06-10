import datetime
import speech_recognition as sr
import os
import requests
import mac_say
import time
import webbrowser
import re
import psutil
from wolframalpha import Client

def speak(audio):
    mac_say.say([audio, "-v", "Alex"])
    os.system('kill `pgrep speechsynthesisd`')
    os.system('pkill speechsynthesisd say')

def print_speak(text):
    print(text)
    speak(text)

def ctime():
    strTime = datetime.datetime.now().strftime("%H houres and %M minutes")
    print_speak(f"Sir, the time is {strTime}")


def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)

# reading battery status
battery = psutil.sensors_battery()
bp = battery.percent
bcp = battery.power_plugged
bt = secs2hours(battery.secsleft)

# create wolframalpha Client
client = Client('')

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        return "Good Morning Sir."
    elif hour >= 12 and hour < 16:
        return "Good Afternoon Sir."
    else:
        return "Good Evening Sir."

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognising...")
        query = r.recognize_google(audio, language="en-us")
        print(f"You said: {query}\n")
    except Exception as e:
        # print_speak("Sorry, please say again")
        return "None"
    return query

def start_task():
    print("Initializing AI Assistant...")
    speak("Initializing AI Assistant")

    # Check the Internet
    url = "https://www.google.com/"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        print("Connectting to the Internet...")
        speak("Connectting to the Internet")
        time.sleep(1)

        print_speak("Internet Connection Detected")
        
        print("Activating the System...")
        speak("Activating the System")
        time.sleep(1)

        print_speak("All Systems have been Activated")
    except (
        requests.exceptions.ConnectionError,
        requests.exceptions.Timeout,
    ) as exceptions:
        print_speak("No internet connection detected.")
        print_speak("Shutting down the program. Thank you for your time.")
        exit()

def task_GUI():
    os.system('kill `pgrep speechsynthesisd`')
    os.system('pkill speechsynthesisd say')
    # clear = lambda: os.system("clear")
    # clear()
    start_task()
    print("\n************* AI Assistant Started *************\n")
    print_speak(wish_me() + " I am your AI Assistant, how may I help you?")
    while True:
        os.system('kill `pgrep speechsynthesisd`')
        os.system('pkill speechsynthesisd say')
        try:
            query = takeCommand().lower()
            if re.match("^say hello.*", query):
                print_speak("Hello, nice to meet you.")
            elif "how are you" in query:
                print_speak("My AI mood levels are always positive. How are you sir?")
            elif 'fine' in query or 'happy' in query or "i'm ok" in query:
                print_speak("It's good to know that you are fine.")
            elif 'not good' in query or 'sad' in query or 'upset' in query:
                print_speak("I am sorry to hear that.")
            # elif re.match(".*what.*time.*", query):
            #     ctime()
            elif "who are you" in query or "about you" in query or "your details" in query or "self introduction" in query or "introduce yourself" in query:
                print_speak("I am the first version of AI Assistant developed by Junjie Hou. I can help a lot just like your friend.")
                print_speak("Today, I am here to assist present the Tech Talk speech.")
            elif re.match(".*check.*[power|system].*", query):
            # print(f"charge = {bp}, time left = {bt}, Charger Plugged-in = {bcp}")
                if bp <= 20:
                    print_speak(
                        f'Battery level is, {bp}  percent! System status: Critical! Time remaining: {bt}. We are now running on backup power! Charger Plugged-in: {bcp}')
                elif bp > 20 and bp <= 59:
                    print_speak(
                        f'Battery level is, {bp} percent! System status: Average!  Time remaining: {bt}. Charger Plugged-in: {bcp}')
                elif bp <= 10:
                    print_speak('Battery level critical!  Time remaining: {bt}. Plugin power supply!')
                elif bp >= 60 and bp <= 99:
                    print_speak(f'Battery level is, {bp} percent! System status: Good!  Time remaining: {bt}. Charger Plugged-in: {bcp}')
                elif bp == 100:
                    print_speak(f'Battery is fully charged! Charger Plugged-in: {bcp}')
            # Open web browser
            elif re.match(".*open .*[presentation|speech].*", query):
                url = "http://127.0.0.1:3000"
                webbrowser.open_new_tab(url)
                print_speak("Website Opened")
            elif re.match(".*open .* price optimization project[s]?.*", query):
                url = "http://127.0.0.1:8002"
                webbrowser.open(url)
            elif re.match(".*open .* customer insight project[s]?.*", query):
                url = "http://127.0.0.1:8003"
                webbrowser.open(url)
            # elif "shutdown" in query:
            #     print_speak("Do you really want to shut down your pc Say Yes or else No")
            #     print_speak("Say Yes or else No")
            #     ans_from_user=takeCommand().lower()
            #     if 'yes' in ans_from_user:
            #         speak('Shutting Down...')
            #         os.system('shutdown -s') 
            #     elif 'no' in ans_from_user:
            #         speak('shutdown abort Speak Again')
            #         takeCommand().lower()
            elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query or "shutdown" in query:
                print_speak('I feeling very sweet after meeting with all of you, have a nice day.')
                exit()
            elif 'what' in query or 'time' in query or 'get' in query or "when" in query or "why" in query or "how" in query or "give" in query or "could" in query:
                try:
                    print_speak('searching...')
                    res = client.query(query)
                    results = next(res.results).text
                    print_speak(results)

                except Exception as e:
                    print(e)
                    print_speak('Sorry Sir! No data, available!')
            elif query != "none" and len(query) > 0:
                print_speak("Sorry, I can not understand,please say again!")
            else:
                continue
        except Exception as e:
            continue
