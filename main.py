import pyttsx3
import datetime
import speech_recognition as sr
import os
import requests

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning sir")
    elif hour >= 12 and hour < 16:
        speak("good afternoon sir")
    else:
        speak("good evening sir")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognising...")
        query = r.recognize_google(audio, language='eng-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)
        print("Unable to recognize your voice")
        return "None"
    return query


if __name__ == "__main__":
    clear = lambda: os.system("clear")
    clear()
    speak("Initializing AI Assistant...")

    # Check the Internet
    url = "https://www.google.com/"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        print("Connected to the Internet")
        speak("internet connection detected")
        speak("all systems have been activated")
    except (
        requests.exceptions.ConnectionError,
        requests.exceptions.Timeout,
    ) as exceptions:
        print("No internet connection")
        speak("No internet connection detected.")
        speak("Shutting down the program. Thank you for your time.")
        exit()
    wish_me()

    while True:
        query = takeCommand().lower()
        if "hello" in query:
            speak("Hello Sir")
            speak("I am your digital assistant. How may I help you?")

        elif "how are you" in query:
            speak("my AI mood levels are always positive")
            speak("how are you sir")

        elif "fine" in query:
            speak("It's good to know that you are fine")

        elif "none" in query:
            speak("unable to recognize your voice")
