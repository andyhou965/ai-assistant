import sys

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
        self.main()

    def main(self):
        # start_task()
        task_GUI()

# Redirect stdout to QTextBrowser
class EmittingStr(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)
    def write(self, text):
        self.textWritten.emit(str(text))

FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"UI/main.ui"))
class Gui_Start(QMainWindow, FROM_MAIN):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Redirect stdout to QTextBrowser
        sys.stdout = EmittingStr(textWritten=self.outputWritten)
        sys.stderr = EmittingStr(textWritten=self.outputWritten)

        self.start_button.clicked.connect(self.startTask)

    def outputWritten(self, text):
        cursor = self.code_browser.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.code_browser.setTextCursor(cursor)
        self.code_browser.ensureCursorVisible()

    def startTask(self):
        self.label1 = QtGui.QMovie("UI/assets/virtual-body.gif")
        self.virtual_body.setMovie(self.label1)
        self.label1.start()

        self.label2 = QtGui.QMovie("UI/assets/chart.gif")
        self.param_board.setMovie(self.label2)
        self.label2.start()

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

if __name__ == "__main__":
    Gui_App = QApplication(sys.argv)
    AI_Gui = Gui_Start()
    AI_Gui.show()
    exit(Gui_App.exec_())
