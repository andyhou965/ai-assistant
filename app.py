import sys
from ui import Ui_AI_Assistant
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from PyQt5.uic import loadUiType
# from utils import *
# import pyttsx3
import mac_say
import datetime
import speech_recognition as sr
import os
import requests

# engine = pyttsx3.init()
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[0].id)
# engine.setProperty("rate", 170)

def speak(audio):
    mac_say.say([audio, "-v", "Alex"])
    # engine.say(audio)
    # engine.runAndWait()


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
    
    def run(self):
        self.main()

    def main(self):
        speak("Hello, I am AI Assistant")
        while True:
            self.query = self.takeCommand().lower()
            if "hello" in self.query:
                speak("Hello Sir")
                speak("I am your digital assistant. How may I help you?")

            elif "how are you" in self.query:
                speak("my AI mood levels are always positive")
                speak("how are you sir")

            elif "fine" in self.query:
                speak("It's good to know that you are fine")

            elif "none" in self.query:
                speak("unable to recognize your voice")


    def wish_me(self):
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("good morning sir")
        elif hour >= 12 and hour < 16:
            speak("good afternoon sir")
        else:
            speak("good evening sir")


    def takeCommand(self):
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



class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gui = Ui_AI_Assistant()
        self.gui.setupUi(self)
       
        self.gui.start_button.clicked.connect(self.startTask)

    def startTask(self):
        self.gui.label1 = QtGui.QMovie("UI/assets/virtual-body.gif")
        self.gui.virtual_body.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie("UI/assets/chart.gif")
        self.gui.param_board.setMovie(self.gui.label2)
        self.gui.label2.start()

        # timer = QTimer(self)
        # timer.timeout.connect(self.showTimeLiver)
        # timer.start(999)
        self.startExe = MainThread()
        self.startExe.start()

    def showTimeLive(self):
        # time = QTime.currentTime().toString()
        # date = QDate.currentDate().toString()
        # label_time = "Time: " + time
        # label_date = "Date: " + date

        # self.gui.text_time.setText(label_time)
        # self.gui.text_date.setText(label_date)
        pass

Gui_App = QApplication(sys.argv)
AI_Gui = Gui_Start()
AI_Gui.show()
exit(Gui_App.exec_())
