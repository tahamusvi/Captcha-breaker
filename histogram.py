import cv2
import numpy as np
from matplotlib import pyplot as plt
from ImageFunctions import *
#--------------------------------------------
def histogram(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()

#--------------------------------------------
# path = "test/ts2/"

# for file_name in os.listdir(path):

histogram("test/ts2/0 (2).png")