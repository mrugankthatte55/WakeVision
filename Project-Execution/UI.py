from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import QPixmap
import cv2
import time
import tensorflow as tf
from tensorflow import keras
import tensorflow as tf
from tensorflow import keras
from pygame import mixer 
import sys
from PIL import Image
from subprocess import call
import validate as validate
import headers as headers
import ROI_Eye as ROI_Eye
import python_pie3D as python_pie3D

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
left_eye_haar=cv2.CascadeClassifier("haarcascade_lefteye_2splits.xml")
right_eye_haar=cv2.CascadeClassifier("haarcascade_righteye_2splits.xml")
window_width=800
window_ht=750


image_path_l="Buffer/left_0.png"
image_path_r="Buffer/right_0.png"
model = keras.models.load_model('model4.h5')

cap = cv2.VideoCapture(0)

class Ui_MainWindow(object):
    temp=0
    def setupUi(self, MainWindow,path):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(863, 677)
        MainWindow.setStyleSheet("background-color: rgb(105, 105, 105);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 863, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.retranslateUi(MainWindow)

    #l1=[]
    #l2=[]
    opentime=0
    closedtime=0
    totaltime=0
    def timechange(self,t):
        return(str(time.strftime('%H:%M:%S', time.gmtime(t))))


    def stopclicked(self):
        print("stop clicked")
        totaltime=time.time()-self.totaltime
        notdetected=totaltime-self.opentime-self.closedtime
        print(" open time: ",self.opentime," alarm time: ",self.closedtime," face not detected: ",notdetected)
        l1=[self.opentime,self.closedtime,notdetected]
        pclosed=(self.closedtime/totaltime)*100
        pnotdetected=(notdetected/totaltime)*100
        popen=(self.opentime/totaltime)*100
        
        l2=[" open time: "+str(round(popen,3))+" %"," alarm time: "+str(round(pclosed,3))+" %"," face not detected: "+str(round(pnotdetected,3))+" %"]
        timestring="open time: "+self.timechange(round(self.opentime,3))+"\nalarm time: "+self.timechange(round(self.closedtime,3))+"\nface not detected: "+self.timechange(round(notdetected,3))+"\n"
        print(time.ctime(totaltime))

        f = open("Drivertime.txt", "w")
        f.write(timestring)
        f.close()
        print(l1,l2)
        python_pie3D.python_pie3D(l1,l2)
        self.temp=1
        QtWidgets.qApp.quit()
        call(["python", "last.py"])
        QtWidgets.qApp.quit()
        

    def retranslateUi(self, MainWindow):
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.pushButton.setText(_translate("MainWindow", "Stop"))
        self.pushButton.clicked.connect(self.stopclicked)

        #print(self.label.width())#100
        #print(self.label.height())#30

        i=0
        cnt=0
        self.totaltime=time.time()
        start=self.totaltime
        flag=1
        
        
        mixer.init()
        mixer.music.load("alarm1.mp3")
        mixer.music.play()
        mixer.music.pause()

        ptime=0
        ctime=0

        while self.temp==0:
            bgrl=[]
            bgrr=[]
            
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            i,bgrl,bgrr=ROI_Eye.ROI_Eye(i,gray)
            path="pie chart.png"
            faces = face_cascade.detectMultiScale(gray, 1.3, 4)
            if len(bgrl)!=0 and len(bgrr)!=0:
                if cnt==5 :
                    img=cv2.resize(cv2.imread("danger.png"),(863, 677))
                    path="danger.png"
                    mixer.music.unpause()
                    if flag==1:
                        self.opentime+=time.time()-start
                        flag=0
                        start=time.time()

                if cnt>0 and (validate.validate(image_path_l)==1 or validate.validate(image_path_r)==1):
                    cnt-=1
                    mixer.music.stop()
                    mixer.music.play()
                    mixer.music.pause()
                    if flag==0:
                        self.closedtime+=time.time()-start
                        flag=1
                        start=time.time()

                if cnt<5 and validate.validate(image_path_l)==0 and validate.validate(image_path_r)==0 :
                    cnt+=1

                if cnt!=5:
                    for (x,y,w,h) in faces:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                cv2.imwrite("Buffer/face.png",img)
                path="Buffer/face.png"


            else:
                path="facenotdetected.png"
                mixer.music.stop()
                mixer.music.play()
                mixer.music.pause()
            if cv2.waitKey(1) & 0xFF == ord('s'):
                
                break
            self.pixmap = QPixmap(path)
            # adding image to label
            self.pixmap = self.pixmap.scaled(863, 677)
            
            self.label.setPixmap(self.pixmap)

            ctime=time.time()
            fps=1/(ctime-ptime)
            ptime=ctime
            print(int(fps))
            MainWindow.show()
        
        
        
        
        
        
        


    
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    path="pie chart.png"
    ui.setupUi(MainWindow,path)
    MainWindow.show()
    MainWindow.close()
    exit()
    sys.exit(app.exec_())
