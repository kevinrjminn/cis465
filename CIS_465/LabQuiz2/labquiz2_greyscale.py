import cv2
import numpy as np
image = cv2.imread("CSU.jpg")
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
    filename = "CSU_greyscale" + str(t) + ".jpg"
    cv2.imwrite(filename, ouput_image)

Thresholding1(70)
Thresholding1(170)

# image = cv2.imread("img.png")

grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

height, width = grayscale.shape