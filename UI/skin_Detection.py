# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UploadVideo.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import tkinter
import tkinter.filedialog
import cv2
from PyQt5 import QtCore, QtGui
from stage import classify_Skin as fs
import os
import sys

root=tkinter.Tk()

print('******Start*****')
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

class Ui_stage2(object):
    

    def setupUii(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        #MainWindow.resize(377, 320)
        MainWindow.resize(1200, 800)
        MainWindow.setStyleSheet(_fromUtf8("\n""background-image: url(SK.jpg);\n"""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 180, 220, 27))
        self.pushButton.clicked.connect(self.quit)
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 128, 0);\n"
"color: rgb(0, 0, 0);"))
       
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
#################################################################
        
######################################################################
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(200, 50, 220, 31))
        
        self.textEdit.setStyleSheet(_fromUtf8("background-color: rgb(255,255,255);\n"
"color: rgb(0, 0, 0);"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 180, 220, 27))
        self.pushButton_2.clicked.connect(self.classify)
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 128, 0);\n"
"color: rgb(0, 0, 0);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        
     
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 120, 220, 27))
        self.pushButton_3.clicked.connect(self.browse)
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color: rgb(255, 128, 0);\n"
"color: rgb(0, 0, 0);"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        

        
        
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 60, 41, 17))
        self.label.setStyleSheet(_fromUtf8("\n"
"color: rgb(0, 0, 0);"))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Skin Cancer Detection", None))
        self.pushButton_3.setText(_translate("MainWindow", "Select Image", None))
        self.pushButton_2.setText(_translate("MainWindow", "Skin Result", None))
        self.pushButton.setText(_translate("MainWindow", "Exit", None))
        self.label.setText(_translate("MainWindow", "Path", None))
        
    def quit(self):
        print ('Process end')
        print ('******End******')
        quit()
        #sys.exit()
       # quit(self.centralwidget)

         
    def browse(self):
        global fileName
        root.withdraw()
        filename = tkinter.filedialog.askopenfilename()
        fileName = filename
        self.textEdit.setText(fileName)
        return fileName
    
    def classify(self):
        print ('Process Start')

        str_1 = fs.classify(self,fileName)
        result = str_1.split('\n')[0]
        res01 = str_1.split('\n')[1]


        print("RE ::", res01)
        #print("RE ::", res02)
        #print("RE ::", res03)

        # res01=str_1.split(")")
        print("\n""Final Result :: ", result)
        res = result.split("(")
        # self.label_1.setText(_translate("MainWindow", "Result : " + str_1.split('\n')[0] + '\n\n' + 'scores are : \n' + str_1, None))
        img = cv2.imread("res.jpg")
        # font
        font = cv2.FONT_HERSHEY_SIMPLEX

        # org
        org1 = (30, 30)
        org2 = (30, 70)


        # fontScale
        fontScale = 1.0

        # Blue color in BGR
        color = (255, 20, 147)

        # Line thickness of 2 px
        thickness = 2
        # new_image=cv2.resizeWindow('img', 600, 600)

        # define the screen resulation
        screen_res = 600, 800
        scale_width = screen_res[0] / img.shape[1]
        scale_height = screen_res[1] / img.shape[0]
        scale = max(scale_width, scale_height)

        # resized window width and height
        window_width = int(img.shape[1] * scale)
        window_height = int(img.shape[0] * scale)

        # cv2.WINDOW_NORMAL makes the output window resizealbe
        cv2.namedWindow('Score Window', cv2.WINDOW_NORMAL)

        # resize the window according to the screen resolution
        cv2.resizeWindow('Score Window', window_width, window_height)

        # Using cv2.putText() method
        image = cv2.putText(img, result, org1, font, fontScale, color, thickness, cv2.LINE_AA)
        image1 = cv2.putText(image, res01, org2, font, fontScale, color, thickness, cv2.LINE_AA)

        # Displaying the image
        cv2.imshow('Score Window', image1)

        img1 = cv2.imread(fileName)
        # Window name in which image is displayed


        # font
        font = cv2.FONT_HERSHEY_SIMPLEX

        # org
        org = (30, 30)

        # fontScale
        fontScale = 0.7

        # Blue color in BGR
        color = (255, 51, 51)

        # Line thickness of 2 px
        thickness = 1
        # new_image=cv2.resizeWindow('img', 600, 600)

        # define the screen resulation
        screen_res = 600, 800
        scale_width = screen_res[0] / img1.shape[1]
        scale_height = screen_res[1] / img1.shape[0]
        scale = min(scale_width, scale_height)

        # resized window width and height
        window_width = int(img1.shape[1] * scale)
        window_height = int(img1.shape[0] * scale)

        # cv2.WINDOW_NORMAL makes the output window resizealbe
        cv2.namedWindow('Result Window', cv2.WINDOW_NORMAL)

        # resize the window according to the screen resolution
        cv2.resizeWindow('Result Window', window_width, window_height)

        # Using cv2.putText() method
        image1 = cv2.putText(img1, res[0], org, font, fontScale, color, thickness, cv2.LINE_AA)

        # Displaying the image
        cv2.imshow('Result Window', image1)
        prec = cv2.imread("p5.jpg")
        cv2.imshow('Skin cancer prevention', prec)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
         
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_stage2()
    ui.setupUii(MainWindow)
    MainWindow.move(550, 170)
    MainWindow.show()
    sys.exit(app.exec_())
    

