# image video and cam trigger(showing)

import cv2
print("Package Imported")
# importing an image
# img = cv2.imread("resources/profile - Copy.png")
# cv2.imshow("Output",img)
# cv2.waitKey(1000)

# importing a video if press q it will close
# cap=cv2.VideoCapture("resources/opencv.mp4")
cap=cv2.VideoCapture(0)
# for height with and brightness
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
while True:
    success,img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

