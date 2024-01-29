# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
import sqlite3
from login import Ui_Dialog
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from tkinter.constants import ALL
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import re
import sys



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

class Ui_signUp(object):
    def insertData(self):
        error=None
        username1 = self.uname_lineEdit.text()
        username=str(username1)
        email1 = self.email_lineEdit.text()
        if email1.find('@') == -1:
            error=True
            self.email_lineEdit.setText('enter vaild email eg:abc@gmail.com')
            self.email_lineEdit.setStyleSheet("color: red")
        else:
            email = str(email1)
            
        mob1= self.mob_lineEdit.text()
        if len(mob1)!=10 or len(re.findall('\D',str(mob1),re.I))>0:
            error=True
            self.mob_lineEdit.setText('please enter valid number')
            self.mob_lineEdit.setStyleSheet("color: red")
        else:
            mob=str(mob1)
        password1 = self.password_lineEdit.text()
        password =str(password1)
        '''
        gender1= self.gender_lineEdit.text()
        gender=str(gender1)
        '''
        gender=''
        if self.b2.isChecked():
            gender='Male'
        if self.b1.isChecked():
            gender='Female'
        
        
        if not error:
            connection = sqlite3.connect("multiD.db")
            s="insert into userdetails (username,email,mob,password,gender) values('"+username+"','"+email+"','"+mob+"','"+password+"','"+gender+"')"
            print("query is:-"+s)
            result=connection.execute(s)
            if result:
                s1="select * from userdetails"
                result=connection.execute(s1)
                print("Success  :: "+s1)
            connection.commit()
            connection.close()
            self.showmsg()

    def showmsg(self):
        self.showdialog()

    def showdialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("Registration Status")
        msg.setInformativeText("Registration Successful")
        msg.setWindowTitle("Status")
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        retval = msg.exec_()
        print
        "value of pressed message box button:", retval

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
    def signInCheck(self):
        print("hello signin button")
        self.signInWindow=QtGui.QDialog()
        self.ui=Ui_Dialog()
        print("i'm in self signin")
        self.ui.setinUi(self.signInWindow)
        print("i'm in self setupUi method")
        self.signInWindow.show()
        print("i'm in self signin windows")
        
    def signInButton(self):
            self.signInCheck()
               
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1300, 800)
        Dialog.setStyleSheet(_fromUtf8("background-image: url(dp3.jpg); border: 2px solid black"))
       # Dialog.setStyleSheet(_fromUtf8("border: 2px solid black"))
   
#############################################################################
 
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 100, 130, 30))
        self.label.setObjectName(_fromUtf8("label"))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
               
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 150, 110, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        
        self.label_M = QtGui.QLabel(Dialog)
        self.label_M.setGeometry(QtCore.QRect(100, 200, 110, 20))
        self.label_M.setObjectName(_fromUtf8("label_M"))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_M.setFont(font)
        
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 250, 130, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        
        self.label_G = QtGui.QLabel(Dialog)
        self.label_G.setGeometry(QtCore.QRect(100, 300, 91, 20))
        self.label_G.setObjectName(_fromUtf8("label_G"))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_G.setFont(font)
        
        self.label_G_M = QtGui.QLabel(Dialog)
        self.label_G_M.setGeometry(QtCore.QRect(240, 300, 70, 20))
        self.label_G_M.setObjectName(_fromUtf8("label_G_M"))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_G_M.setFont(font)
        
        
        self.label_G_F = QtGui.QLabel(Dialog)
        self.label_G_F.setGeometry(QtCore.QRect(355, 300, 100, 20))
        self.label_G_F.setObjectName(_fromUtf8("label_G_F"))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_G_F.setFont(font)
        
        #############################################################

        
        self.uname_lineEdit = QtGui.QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QtCore.QRect(215, 100, 211, 27))
        self.uname_lineEdit.setObjectName(_fromUtf8("uname_lineEdit"))
        
        '''
        reg_ex = QRegExp("[0-9]*@.?[a-z]*/.?[a-z]")
        input_validator = QRegExpValidator(reg_ex, self.uname_lineEdit)
        self.uname_lineEdit.setValidator(input_validator)
        '''
        
        
        self.email_lineEdit = QtGui.QLineEdit(Dialog)
        self.email_lineEdit.setGeometry(QtCore.QRect(215, 150, 211, 27))
        self.email_lineEdit.setObjectName(_fromUtf8("email_lineEdit"))
        
        self.mob_lineEdit = QtGui.QLineEdit(Dialog)
        self.mob_lineEdit.setGeometry(QtCore.QRect(215, 200, 211, 27))
        self.mob_lineEdit.setObjectName(_fromUtf8("mob_lineEdit"))
        
        self.password_lineEdit = QtGui.QLineEdit(Dialog)
        self.password_lineEdit.setGeometry(QtCore.QRect(215, 250, 211, 27))
        self.password_lineEdit.setObjectName(_fromUtf8("password_lineEdit"))
        self.password_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        
        '''
        self.gender_lineEdit = QtGui.QLineEdit(Dialog)
        self.gender_lineEdit.setGeometry(QtCore.QRect(215, 300, 211, 27))
        self.gender_lineEdit.setObjectName(_fromUtf8("gender_lineEdit"))
        '''
        
        self.b2 = QtGui.QRadioButton(Dialog)
        self.b2.setObjectName(_fromUtf8("Male"))
        self.b2.setGeometry(QtCore.QRect(215, 300, 18, 20))
        self.b2.toggled.connect(lambda:self.btnstate(self.b2))
        self.b2.setText('Male')
        self.b2.setChecked(True)
        
        self.b1 = QtGui.QRadioButton(Dialog)
        self.b1.setObjectName(_fromUtf8("Female"))
        self.b1.setGeometry(QtCore.QRect(330, 300, 18, 20))
        self.b1.toggled.connect(lambda:self.btnstate(self.b1))
        self.b1.setText('Female')
        
        self.email_lineEdit.setStyleSheet("color: black")
        self.mob_lineEdit.setStyleSheet("color: black")
        
        ###################################################################
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(217, 25, 320, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        
        self.signup_btn = QtGui.QPushButton(Dialog)
        self.signup_btn.setGeometry(QtCore.QRect(218, 350, 95, 27))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.signup_btn.setFont(font)
        self.signup_btn.setObjectName(_fromUtf8("signup_btn"))
        self.signup_btn.setStyleSheet("background-color: black")
        #########################EVENT##############
        self.signup_btn.clicked.connect(self.insertData)
############################################
        
        self.login_btn = QtGui.QPushButton(Dialog)
        self.login_btn.setGeometry(QtCore.QRect(338, 350, 90, 27))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.login_btn.setFont(font)
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
        self.login_btn.setStyleSheet("background-color: black")
        self.login_btn.clicked.connect(self.signInButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
        
    
    def btnstate(self,b):
        if b.text() == "Male":
            if b.isChecked() == True:
                print( b.text()+" is selected")
            else:
                print (b.text()+" is deselected")
                  
        if b.text() == "Female":
            if b.isChecked() == True:
                print (b.text()+" is selected")
            else:
                print (b.text()+" is deselected")
     
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        
  
        self.label.setText(_translate("Dialog", "USERNAME", None))
        self.label_2.setText(_translate("Dialog", "EMAIL ID", None))
        self.label_M.setText(_translate("Dialog", "MOBILE", None))
        self.label_3.setText(_translate("Dialog", "PASSWORD", None))
        self.label_G.setText(_translate("Dialog", "GENDER", None))
        
        self.label_G_M.setText(_translate("Dialog", "Male", None))
        self.label_G_F.setText(_translate("Dialog", "Female", None))
        
        self.label_4.setText(_translate("Dialog", "Registration Form", None))
        self.signup_btn.setText(_translate("Dialog", "Sign Up", None))
        self.login_btn.setText(_translate("Dialog", "Login", None))
      
   


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_signUp()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

