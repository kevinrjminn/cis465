import cv2
import numpy as np

from matplotlib import pyplot as plt
def myHist(img):
    row, col = img.shape #image is grey scale image
    y=np.zeros(256)
    for i in range(0, row):
        for j in range (0, col):
            y[img[i,j]] += 1
    # x = np.arange (0,256)
    x = np.arange(0, 256)
    plt.bar(x,y)#color="blue", align="center")
    #plot.plot(x,y)
    cv2.imshow('img', img)
    plt.show()


img = cv2.imread('img.png',0)
# img.show()
cv2.imshow('img',img)
myHist(img)