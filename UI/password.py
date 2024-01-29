# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sqlite3


#from GetPass import pass as ps

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

class Ui_passCheck(object):

        
    def loginCheck(self):
        
        password = ""
        
        username1=self.uname_lineEdit.text()
        username =str(username1)
        
        connection=sqlite3.connect("multiD.db")
        s="select *from userdetails where username='"+username+"'"
        print("query is:"+s)
        result=connection.execute(s)
        t=result.fetchall()
        if(len(t)>0):
            password = t[0][3]
            print(password)
            #print(t[3])
            print("user found!")
            pass_str = "Hi {}! your password is: {}".format(username, password)
            
            #ps.pass(self,username)
            #return self.password          
        else:
            print("user not found!")
            password = "user not found!"
            pass_str = "Sorry, user not found!"
            #return self.password
        #pass_str = "Hi {}! your password is: {}".format(username, password)
        self.pass_label.setText(_translate("Dialog", pass_str, None))
         
        
    def setinUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(537, 373)
        Dialog.setStyleSheet(_fromUtf8("QDialog{\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 127, ), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"QLineEdit{\n"
"border:none;\n"
"    background-color: rgb(255, 255, 255);\n"
"}"))
        self.u_user_label = QtGui.QLabel(Dialog)
        self.u_user_label.setGeometry(QtCore.QRect(90, 150, 91, 31))
        self.u_user_label.setObjectName(_fromUtf8("u_user_label"))
        
        self.pass_label = QtGui.QLabel(Dialog)
        self.pass_label.setGeometry(QtCore.QRect(190, 200, 201, 31))
        self.pass_label.setObjectName(_fromUtf8("pass_label"))

       
        
        self.uname_lineEdit = QtGui.QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QtCore.QRect(190, 149, 201, 31))
        self.uname_lineEdit.setText(_fromUtf8(""))
        self.uname_lineEdit.setObjectName(_fromUtf8("uname_lineEdit"))
       

        
        
        self.login_btn = QtGui.QPushButton(Dialog)
        self.login_btn.setGeometry(QtCore.QRect(210, 250, 120, 31))
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
       #####################Button Event####################################
        self.login_btn.clicked.connect(self.loginCheck)
       ############################################################################
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(230, 90, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Forgote Password", None))
        self.u_user_label.setText(_translate("Dialog", "Enter USERNAME", None))
        #self.pass_label.setText(_translate("Dialog", self.password, None))
      
        self.login_btn.setText(_translate("Dialog", "Get Password", None))
        self.label.setText(_translate("Dialog", "Relogin", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_passCheck()
    ui.setinUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())