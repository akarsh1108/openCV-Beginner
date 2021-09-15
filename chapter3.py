# Sizing and Cropping of Images

import cv2
import numpy as np
img=cv2.imread("Resources/profile - Copy.png")
print(img.shape)
# resizing the shape of the image
imgResize=cv2.resize(img,(200,300))
print(imgResize.shape)
imgCropped=img[0:340,200:500]
cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped ",imgCropped)
cv2.waitKey(15000)