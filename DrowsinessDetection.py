#import ROI_Eye
import numpy as np
import cv2
import time
import tensorflow as tf
from tensorflow import keras
from keras import preprocessing
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Activation, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from pygame import mixer 


from tensorflow.keras.applications import imagenet_utils
from sklearn.metrics import confusion_matrix
import sys
import itertools
import os
import shutil
import random

from PIL import Image


face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
left_eye_haar=cv2.CascadeClassifier("haarcascade_lefteye_2splits.xml")
right_eye_haar=cv2.CascadeClassifier("haarcascade_righteye_2splits.xml")
window_width=800
window_ht=750

cap = cv2.VideoCapture(0)
#0------> closed eyes
#1------> open eyes


image_path_l="Buffer/left_0.png"
image_path_r="Buffer/right_0.png"
model = keras.models.load_model('model2.h5')

def ROI_Eye(i,gray):
    bgrl=[]
    bgrr=[]
    imgleft=[]
    imgright=[]
    left_eye=left_eye_haar.detectMultiScale(gray,1.3,5)
    right_eye=right_eye_haar.detectMultiScale(gray,1.3,5)  
    if len(left_eye)!=0 and len(right_eye)!=0:
        for (lx,ly,lw,lh) in left_eye:
            roi_l=gray[ly:ly+lh,lx:lx+lw]
            imgleft=cv2.resize(roi_l,(224,224))
            cv2.imwrite("Buffer/left_"+str(i)+".png",imgleft)
        #i+=1
        for (rx,ry,rw,rh) in right_eye:
            roi_r=gray[ry:ry+rh,rx:rx+rw]
            imgright=cv2.resize(roi_r,(224,224))
            cv2.imwrite("Buffer/right_"+str(i)+".png",imgright)
        #i+=1
        bgrl = cv2.cvtColor(imgleft, cv2.COLOR_GRAY2RGB)
        bgrr = cv2.cvtColor(imgright, cv2.COLOR_GRAY2RGB)
        bgrl=cv2.resize(bgrl,(224,224))
        bgrr=cv2.resize(bgrr,(224,224))
    return(i,imgleft,imgright)


def validate(image_path):
  image = tf.keras.preprocessing.image.load_img(image_path, grayscale=False, color_mode="rgb", target_size=(224,224), interpolation="nearest")
  input_arr = keras.preprocessing.image.img_to_array(image)
  input_arr = np.array([input_arr])
  input_arr = tf.keras.applications.mobilenet.preprocess_input(input_arr)
  predictions = model.predict(input_arr)
  return round(predictions[0][0])



i=0
cnt=0
totaltime=time.time()
start=time.time()
flag=1
temp=0
opentime=0
closedtime=0
mixer.init()
mixer.music.load('west_coast.mp3')
mixer.music.play()
mixer.music.pause()
while 1:
    bgrl=[]
    bgrr=[]
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    i,bgrl,bgrr=ROI_Eye(i,gray)
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    if len(bgrl)!=0 and len(bgrr)!=0:
        if cnt==5 :
            print("alarm")

            img=cv2.resize(cv2.imread("danger.png"),(window_width,window_ht))
            mixer.music.unpause()
            if flag==1:
                opentime+=time.time()-start
                print("Open time ---> ",time.time()-start)
                flag=0
                start=time.time()

        if cnt>0 and (validate(image_path_l)==1 or validate(image_path_r)==1):
            cnt-=1
            mixer.music.stop()
            mixer.music.play()
            mixer.music.pause()
            if flag==0:
                closedtime+=time.time()-start
                print("Alarm time ---> ",time.time()-start)
                flag=1
                start=time.time()

        if cnt<5 and validate(image_path_l)==0 and validate(image_path_r)==0 :
            cnt+=1
            
            
            
        print(cnt)
        if cnt!=5:
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow("face",cv2.resize(img,(window_width,window_ht)))

    else:
        facenotdetected=cv2.resize(cv2.imread("facenotdetected.png"),(window_width,window_ht))
        cv2.imshow("face",facenotdetected)
        mixer.music.stop()
        mixer.music.play()
        mixer.music.pause()
    if cv2.waitKey(1) & 0xFF == ord('s'):
        totaltime=time.time()-totaltime
        break
cap.release()
cv2.destroyAllWindows()
notdetected=totaltime-opentime-closedtime
print(" open time: ",opentime," alarm time: ",closedtime," totaltime: ",totaltime," face not detected: ",notdetected)
