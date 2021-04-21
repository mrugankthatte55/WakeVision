from subprocess import call
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
#import headers
from cv2 import *
from PyQt5.QtGui import QPixmap

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.now = datetime.now()
        self.dt_string = self.now.strftime("%d/%m/%Y %H:%M:%S")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(475, 200)
        MainWindow.setStyleSheet("background-color: rgb(105, 105, 105);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(150, 60, 121, 121))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 10, 140, 30))
        self.label_3.setStyleSheet("border-color: rgb(255, 170, 0);background-color: rgb(255, 170, 0);")
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(150, 60, 260, 50))
        self.textEdit.setStyleSheet("border-color: rgb(255, 170, 0);color:white;font-size: 20px;")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 140, 75, 23))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 0);border-color: rgb(47, 147, 215);")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 120, 50))
        self.label_2.setStyleSheet("border-color: rgb(47, 147, 215);background-color: rgb(255, 170, 0);")
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Driver's Name:")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def buttonclicked(self,MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("MainWindow", "running"))
        textboxValue = self.textEdit.toPlainText()
        f = open("Driverinfo.txt", "w")
        f.write("Name: "+str(textboxValue)+"\n")
        f.write("Date: "+self.dt_string[:10]+"\n")
        f.close()
        print(textboxValue)
        QtWidgets.qApp.quit()
        call(["python", "UI.py"])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.pushButton.clicked.connect(self.buttonclicked)

        print(self.dt_string)
        self.label_3.setText(self.dt_string)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
