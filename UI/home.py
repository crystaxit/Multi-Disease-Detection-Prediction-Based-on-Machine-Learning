# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
from signup import Ui_signUp 
from login import Ui_Dialog

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

class Ui_MainWindow(object):
    
    def aboutButton(self):
            self.aboutCheck()   
    def aboutCheck(self):
        print("hello about button")
        self.signUpWindow=QtGui.QDialog()
        #self.ui=Ui_about()
        print("i'm in self about")
        self.ui.setupUi(self.signUpWindow)
        print("i'm in self setupUi method")
        self.signUpWindow.show()
        print("i'm in self about windows")
        
    def signUpCheck(self):
        print("hello signup button")
        self.signUpWindow=QtGui.QDialog()
        self.ui=Ui_signUp()
        print("i'm in self signup")
        self.ui.setupUi(self.signUpWindow)
        print("i'm in self setupUi method")
        self.signUpWindow.show()
        print("i'm in self signup windows")
          
    def signInCheck(self):
        print("hello signin button")
        self.signInWindow=QtGui.QDialog()
        self.ui=Ui_Dialog()
        print("i'm in self signin")
        self.ui.setinUi(self.signInWindow)
        print("i'm in self setupUi method")
        self.signInWindow.show()
        print("i'm in self signin windows")
            
        
        
    def signUpButton(self):
            self.signUpCheck()
    
    def signInButton(self):
            self.signInCheck()
     
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWin41dow"))
        MainWindow.resize(1200, 900)
        MainWindow.setStyleSheet(_fromUtf8("\n"
"background-image: url(hm.jpg);\n"
""))
    
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))


        #############################################################################
        self.sign_up1 = QtGui.QPushButton(self.centralwidget)
        self.sign_up1.setGeometry(QtCore.QRect(350, 30, 250, 40))
        self.sign_up1.setObjectName(_fromUtf8("sign_up1"))
        ##############################################################################
        self.sign_up1.clicked.connect(self.signUpButton)
        ###################################################################################
        self.sign_in1 = QtGui.QPushButton(self.centralwidget)
        self.sign_in1.setGeometry(QtCore.QRect(650, 30, 250, 40))
        self.sign_in1.setObjectName(_fromUtf8("sign_in1"))
        ##############################################################################
        self.sign_in1.clicked.connect(self.signInButton)
        ###################################################################################
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "HOME PAGE", None))

        self.sign_up1.setText(_translate("MainWindow", "SignUp", None))
        self.sign_in1.setText(_translate("MainWindow", "SignIn", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

