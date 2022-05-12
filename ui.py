# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


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
        self.param_board = QtWidgets.QLabel(self.centralwidget)
        self.param_board.setGeometry(QtCore.QRect(720, 150, 691, 241))
        self.param_board.setText("")
        self.param_board.setPixmap(QtGui.QPixmap("UI/assets/chart.gif"))
        self.param_board.setScaledContents(False)
        self.param_board.setObjectName("param_board")
        self.menu = QtWidgets.QLabel(self.centralwidget)
        self.menu.setGeometry(QtCore.QRect(530, 10, 411, 51))
        self.menu.setText("")
        self.menu.setPixmap(QtGui.QPixmap("UI/assets/army.png"))
        self.menu.setScaledContents(True)
        self.menu.setObjectName("menu")
        self.virtual_body = QtWidgets.QLabel(self.centralwidget)
        self.virtual_body.setGeometry(QtCore.QRect(20, 110, 681, 771))
        self.virtual_body.setText("")
        self.virtual_body.setPixmap(QtGui.QPixmap("UI/assets/virtual-body.gif"))
        self.virtual_body.setScaledContents(True)
        self.virtual_body.setObjectName("virtual_body")
        self.code_panel = QtWidgets.QLabel(self.centralwidget)
        self.code_panel.setGeometry(QtCore.QRect(660, 350, 781, 641))
        self.code_panel.setText("")
        self.code_panel.setPixmap(QtGui.QPixmap("UI/assets/code-border.png"))
        self.code_panel.setScaledContents(True)
        self.code_panel.setObjectName("code_panel")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(30, 10, 81, 41))
        self.start_button.setStyleSheet("background-color: Transparent;\n"
            "border-radius: none;\n"
            "font-weight: bold;\n"
            "color: rgb(22, 178, 214);\n"
            "font: 15pt \"Arial\";\n"
        "")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/assets/power_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.start_button.setIcon(icon)
        self.start_button.setIconSize(QtCore.QSize(32, 32))
        self.start_button.setObjectName("start_button")
        self.main_bg.raise_()
        self.start_button.raise_()
        self.menu.raise_()
        self.virtual_body.raise_()
        self.code_panel.raise_()
        self.param_board.raise_()
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
