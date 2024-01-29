# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomePage.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
from UploadImage import Ui_MainWindow
from stage_Detection import Ui_stage
from tumer_Detection import Ui_stage1
from skin_Detection import Ui_stage2

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_HomePage(object):
    def setupUi(self, HomePage):
        HomePage.setObjectName(_fromUtf8("HomePage"))
        HomePage.resize(1200, 800)
        HomePage.setStyleSheet(_fromUtf8("\n""background-image: url(bt.jpg);\n"""))
        self.centralwidget = QtGui.QWidget(HomePage)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 80, 240, 41))
        self.pushButton.clicked.connect(self.Ui_stage1)
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(51, 255, 51);\n"
"color: rgb(0, 0, 0);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(800, 80, 240, 41))
        self.pushButton_2.clicked.connect(self.Ui_stage)
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(51, 255, 51);\n"
"color: rgb(0, 0, 0);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 170, 240, 41))
        self.pushButton_3.clicked.connect(self.Ui_stage2)
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color: rgb(51, 255, 51);\n"
"color: rgb(0, 0, 0);"))
        
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(800, 170, 240, 41))
        self.pushButton_4.clicked.connect(self.upload)
        self.pushButton_4.setStyleSheet(_fromUtf8("background-color: rgb(51, 255, 51);\n"
                                                  "color: rgb(0, 0, 0);"))

        self.pushButton_4.setObjectName(_fromUtf8("pushButton_5"))

        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(310, 260, 240, 41))
        self.pushButton_5.clicked.connect(self.quit)
        self.pushButton_5.setStyleSheet(_fromUtf8("background-color: rgb(51, 255, 51);\n"
                                                  "color: rgb(0, 0, 0);"))




        HomePage.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(HomePage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        HomePage.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(HomePage)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        HomePage.setStatusBar(self.statusbar)

        self.retranslateUi(HomePage)
        QtCore.QMetaObject.connectSlotsByName(HomePage)

    def retranslateUi(self, HomePage):
        HomePage.setWindowTitle(_translate("HomePage", "MainWindow", None))
        self.pushButton.setText(_translate("HomePage", "Brain Tumor Detection", None))
        self.pushButton_2.setText(_translate("HomePage", "Lung Cancer Detection", None))
        self.pushButton_3.setText(_translate("HomePage", "Skin Cancer Classification", None))
        self.pushButton_4.setText(_translate("HomePage", "Image Processing", None))
        self.pushButton_5.setText(_translate("HomePage", "Exit", None))

    def upload(self):
        self.videoWindow=QtGui.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUii(self.videoWindow)
        self.videoWindow.show()

    def upload1(self):
        self.videoWindow=QtGui.QMainWindow()
        self.ui=Ui_MainWindow1()
        self.ui.setupUii(self.videoWindow)
        self.videoWindow.show()
       
    def Ui_stage(self):
        self.videoWindow=QtGui.QMainWindow()
        self.ui=Ui_stage()
        self.ui.setupUii(self.videoWindow)
        self.videoWindow.show()

    def Ui_stage1(self):
        self.videoWindow = QtGui.QMainWindow()
        self.ui = Ui_stage1()
        self.ui.setupUii(self.videoWindow)
        self.videoWindow.show()

    def Ui_stage2(self):
        self.videoWindow = QtGui.QMainWindow()
        self.ui = Ui_stage2()
        self.ui.setupUii(self.videoWindow)
        self.videoWindow.show()

    def quit(self):
        print ('Process end')
        print ('******End******')
        quit()

        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    HomePage = QtGui.QMainWindow()
    ui = Ui_HomePage()
    ui.setupUi(HomePage)
    HomePage.move(550, 170)
    HomePage.show()
    sys.exit(app.exec_())

