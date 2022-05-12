import sys
from ui import Ui_AI_Assistant
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from PyQt5.uic import loadUiType
from utils import *
class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        task_GUI()

startExe = MainThread()

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

        startExe.start()

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
