from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AI_Assistant(object):
    def setupUi(self, AI_Assistant):
        AI_Assistant.setObjectName("AI_Assistant")
        AI_Assistant.resize(1442, 961)
        self.centralwidget = QtWidgets.QWidget(AI_Assistant)
        self.centralwidget.setObjectName("centralwidget")
        self.main_bg = QtWidgets.QLabel(self.centralwidget)
        self.main_bg.setGeometry(QtCore.QRect(-10, -10, 1481, 971))
        self.main_bg.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.main_bg.setObjectName("main_bg")
        self.core_frame = QtWidgets.QLabel(self.centralwidget)
        self.core_frame.setGeometry(QtCore.QRect(630, 120, 691, 381))
        self.core_frame.setText("")
        self.core_frame.setPixmap(QtGui.QPixmap("UI/assets/tuse.png"))
        self.core_frame.setScaledContents(True)
        self.core_frame.setObjectName("core_frame")
        self.Gif_core = QtWidgets.QLabel(self.centralwidget)
        self.Gif_core.setGeometry(QtCore.QRect(810, 220, 331, 181))
        self.Gif_core.setText("")
        self.Gif_core.setPixmap(QtGui.QPixmap("UI/assets/core.gif"))
        self.Gif_core.setScaledContents(True)
        self.Gif_core.setObjectName("Gif_core")
        self.menu = QtWidgets.QLabel(self.centralwidget)
        self.menu.setGeometry(QtCore.QRect(910, 20, 411, 51))
        self.menu.setText("")
        self.menu.setPixmap(QtGui.QPixmap("UI/assets/army.png"))
        self.menu.setScaledContents(True)
        self.menu.setObjectName("menu")
        self.ai_face = QtWidgets.QLabel(self.centralwidget)
        self.ai_face.setGeometry(QtCore.QRect(100, 60, 611, 481))
        self.ai_face.setText("")
        self.ai_face.setPixmap(QtGui.QPixmap("UI/assets/ai-face.gif"))
        self.ai_face.setScaledContents(True)
        self.ai_face.setObjectName("ai_face")
        self.code_panel = QtWidgets.QLabel(self.centralwidget)
        self.code_panel.setGeometry(QtCore.QRect(20, 430, 1371, 641))
        self.code_panel.setText("")
        self.code_panel.setPixmap(QtGui.QPixmap("UI/assets/code-border.png"))
        self.code_panel.setScaledContents(True)
        self.code_panel.setObjectName("code_panel")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(1350, 21, 61, 41))
        self.start_button.setStyleSheet("background-color: rgba(33, 255, 220, 204);\n"
"border-radius: 6px;\n"
"color: rgb(0,0,0);\n"
"font-weight: bold;\n"
"selection-background-color: rgba(14, 121, 255, 204);\n"
"selection-color: rgb(255, 255, 255);\n"
"")
        self.start_button.setObjectName("start_button")
        self.main_bg.raise_()
        self.start_button.raise_()
        self.Gif_core.raise_()
        self.core_frame.raise_()
        self.menu.raise_()
        self.ai_face.raise_()
        self.code_panel.raise_()
        AI_Assistant.setCentralWidget(self.centralwidget)

        self.retranslateUi(AI_Assistant)
        QtCore.QMetaObject.connectSlotsByName(AI_Assistant)

    def retranslateUi(self, AI_Assistant):
        _translate = QtCore.QCoreApplication.translate
        AI_Assistant.setWindowTitle(_translate("AI_Assistant", "MainWindow"))
        self.main_bg.setText(_translate("AI_Assistant", "TextLabel"))
        self.start_button.setText(_translate("AI_Assistant", "START"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AI_Assistant = QtWidgets.QMainWindow()
    ui = Ui_AI_Assistant()
    ui.setupUi(AI_Assistant)
    AI_Assistant.show()
    sys.exit(app.exec_())
