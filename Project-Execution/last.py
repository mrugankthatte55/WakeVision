from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import QPixmap
import time
class Ui_DriveReview(object):
    def setupUi(self, DriveReview):
        DriveReview.setObjectName("DriveReview")
        DriveReview.resize(1000, 600)
        DriveReview.setStyleSheet("background-color: rgb(105, 105, 105);")
        self.centralwidget = QtWidgets.QWidget(DriveReview)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 80, 867.5, 300))
        self.label.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 10, 300, 50))
        self.label_2.setStyleSheet("background-color: rgb(255, 170, 0);font-size: 20px;font-family: Courier;")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(355, 400, 320, 100))
        self.label_3.setStyleSheet("background-color: rgb(255, 170, 0);padding: 15px 15px 15px 15px;font-size: 15px;")
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_3.setObjectName("label_3")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 520, 160, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 0);")
        DriveReview.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DriveReview)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 465, 22))
        self.menubar.setObjectName("menubar")
        DriveReview.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DriveReview)
        self.statusbar.setObjectName("statusbar")
        DriveReview.setStatusBar(self.statusbar)

        self.retranslateUi(DriveReview)
        QtCore.QMetaObject.connectSlotsByName(DriveReview)
    

    def retranslateUi(self, DriveReview):
        f = open("Driverinfo.txt", "r")
        name=f.readline()[6:].rstrip()
        disp=f.readline()
        f.close()
        f = open("Drivertime.txt", "r")
        
        for i in range(4):
            disp+=f.readline()
        f.close()
        _translate = QtCore.QCoreApplication.translate
        DriveReview.setWindowTitle(_translate("DriveReview", "MainWindow"))
        self.label_2.setText(_translate("DriveReview", name.upper()))
        self.label_3.setText(_translate("DriveReview", disp))
        self.pushButton.setText(_translate("DriveReview", "Exit"))
        self.pixmap = QPixmap("pie chart.png")
             # adding image to label
        self.pixmap = self.pixmap.scaled(863, 677, QtCore.Qt.KeepAspectRatio)
         
        self.label.setPixmap(self.pixmap)

        self.pushButton.clicked.connect(QtWidgets.qApp.quit)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DriveReview = QtWidgets.QMainWindow()
    ui = Ui_DriveReview()
    ui.setupUi(DriveReview)
    DriveReview.show()
    sys.exit(app.exec_())
