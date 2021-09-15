# Shapes and texts

import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
# print(img.shape)
# # To color it partly
# img[100:300,100:200]=0,255,0
# #To color the whole image
# img[:]=0,255,0
# First is starting coordinate second is size third is colour and last is thickness
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
cv2.rectangle(img,(0,0),(305,325),(0,0,255),3)
cv2.circle(img,(400,50),30,(255,255,0),5)
# we can add text also here 1st image 2nd writing 3rd co ordinates 4th font 5th size 6 colour 7 th thickness
cv2.putText(img,"OPENCV ",(300,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,150,0),1)
cv2.imshow("Image",img)
cv2.waitKey(4000)