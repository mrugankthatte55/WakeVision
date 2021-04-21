from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import QPixmap
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
from pygooglechart import PieChart3D

from tensorflow.keras.applications import imagenet_utils
from sklearn.metrics import confusion_matrix
import sys
import itertools
import os
import shutil
import random
from PIL import Image

from subprocess import call

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
left_eye_haar=cv2.CascadeClassifier("haarcascade_lefteye_2splits.xml")
right_eye_haar=cv2.CascadeClassifier("haarcascade_righteye_2splits.xml")
window_width=800
window_ht=750


image_path_l="Buffer/left_0.png"
image_path_r="Buffer/right_0.png"
model = keras.models.load_model('model4.h5')

def funct():
    pass
    return(0)