# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hands-on-game-home.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from hands_on_game import Ui_Form

class Ui_Home(object):

    def open_second_window(self):
        self.window2 = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.resize(625, 425)
        Home.setMinimumSize(QtCore.QSize(625, 425))
        Home.setMaximumSize(QtCore.QSize(625, 425))
        Home.setStyleSheet("background-color: rgb(88, 79, 135);")
        self.centralwidget = QtWidgets.QWidget(Home)
        self.centralwidget.setStyleSheet("color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, -70, 571, 241))
        self.frame.setStyleSheet("background-image: url(title.png);\n"
"border: none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(30, 180, 281, 281))
        self.frame_2.setMinimumSize(QtCore.QSize(100, 100))
        self.frame_2.setStyleSheet("image: url(01.png);\n"
"border: none;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 290, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Mukti")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(250, 231, 93);\n"
"    border-radius: 15px;\n"
"    color: rgb(88, 79, 135);\n"
"    letter-spacing: 5px;\n"
"    font-style: extrabold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(250, 231, 93, 0.7);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200, 180, 80);  \n"
"    border: 1px solid rgb(120, 100, 40);  \n"
"}\n"
"")

        self.pushButton.setObjectName("pushButton")
        Home.setCentralWidget(self.centralwidget)

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)
        self.pushButton.clicked.connect(self.open_second_window)

    def retranslateUi(self, Home):
        _translate = QtCore.QCoreApplication.translate
        Home.setWindowTitle(_translate("Home", "Hands On Game"))
        self.pushButton.setText(_translate("Home", "INICIAR"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Home = QtWidgets.QMainWindow()
    ui = Ui_Home()
    ui.setupUi(Home)
    Home.show()
    sys.exit(app.exec_())
