import cv2
import numpy as np
image = cv2.imread("pencils.jpg")
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

height, width = grayscale.shape
def Thresholding1(t):
    ouput_image = np.zeros((height, width))
    for i in range(0, height - 1):
        for j in range(0, width - 1):
            if (grayscale[i][j] < t):
                ouput_image[i][j] = 0
            elif (grayscale[i][j] >= t):
                ouput_image[i][j] = 255
    filename = "Img1" + str(t) + ".jpg"
    cv2.imwrite(filename, ouput_image)

Thresholding1(70)
Thresholding1(170)

# image = cv2.imread("pencils.jpg")

grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

height, width = grayscale.shape


def Thresholding2(t1, t2):
    ouput_image = np.zeros((height, width))
    for i in range(0, height - 1):
        for j in range(0, width - 1):
            if (grayscale[i][j] < t1):
                ouput_image[i][j] = 0
            elif (t1 <= grayscale[i][j] <= t2):
                ouput_image[i][j] = grayscale[i][j]
            elif (grayscale[i][j] > t2):
                ouput_image[i][j] = 0

    filename = "Img2" + str(t1) + "-" + str(t2) + ".jpg"
    cv2.imwrite(filename, ouput_image)


Thresholding2(70, 170)
# import cv2
# import numpy as np
# import math
# image = cv2.imread("pencils.jpg")
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
height, width = grayscale.shape

def PowerLawTransform(c, gama):
    ouput_image = np.zeros((height, width))
    for i in range(0, height - 1):
        for j in range(0, width - 1):
            ouput_image[i][j] = c * pow(grayscale[i][j], gama)

    filename = "img3" + " c= " + str(c) + ".jpg"
    cv2.imwrite(filename, ouput_image)


# for C=4  and gama=1
PowerLawTransform(4, .7)