#Warp prespective
import cv2
import numpy as np
img=cv2.imread("resources/cards.jpg")
print(img.shape)

width,height=250,350
pts1=np.float32([[954,41],[1245,41],[954,442],[1245,442]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOutput=cv2.warpPerspective(img,matrix,(width,height))

# cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)
cv2.waitKey(4000)