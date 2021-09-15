# Image detector and functions

import cv2
import  numpy as np
img =cv2.imread("resources/profile - Copy.png")
kernal=np.ones((5,5),np.uint8)
# converting to grayscale
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Blur ksize should be odd
imgBlur=cv2.GaussianBlur(imgGray,(9,9),0)
#Edge Detecter
imgCanny =cv2.Canny(img,120,120)
#Image dilation
imgDilation=cv2.dilate(imgCanny,kernal,iterations=1)
imgEroded=cv2.erode(imgDilation,kernal,iterations=1)
cv2.imshow("Gray image",imgGray)
cv2.imshow("Blur image",imgBlur)
cv2.imshow("Canny image",imgCanny)
cv2.imshow("Dilation image",imgDilation)
cv2.imshow("Eroded image",imgEroded)
cv2.waitKey(5000)