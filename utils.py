import datetime
import speech_recognition as sr
import os
import requests
import mac_say
import time

def speak(audio):
    mac_say.say([audio, "-v", "Alex"])

def print_speak(text):
    print(text)
    speak(text)

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print_speak("Good Morning Sir")
    elif hour >= 12 and hour < 16:
        print_speak("Good Afternoon Sir")
    else:
        print_speak("Good Evening Sir")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognising...")
        query = r.recognize_google(audio, language="en-HK")
        print(f"You said: {query}\n")
    except Exception as e:
        # print(e)
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
    # clear = lambda: os.system("clear")
    # clear()
    print("\n************* AI Assistant Started *************\n")
    wish_me()
    while True:
        query = takeCommand().lower()
        if "hello" in query:
            print_speak("Hello Sir")
            print_speak("I am your digital assistant. How may I help you?")

        elif "how are you" in query:
            print_speak("My AI mood levels are always positive.")
            print_speak("How are you sir?")

        elif "fine" in query:
            print_speak("It's good to know that you are fine.")

        elif "none" in query:
            pass
            # print("Unable to recognize your voice, please try again!")
