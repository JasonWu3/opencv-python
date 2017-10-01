import  cv2
import numpy as np
img=cv2.imread("apple.jpg")
HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
H, S, V = cv2.split(HSV)#RGB转为 HSV
Lowerred = np.array([155,70,46])
Upperred = np.array([180,255,255])
mask = cv2.inRange(HSV, Lowerred, Upperred)
Lowerred1 = np.array([0,70,46])
Upperred1 = np.array([11,255,255])
mask1 = cv2.inRange(HSV, Lowerred1, Upperred1)
mask2 = mask +mask1
#cv2.imshow('s',mask2)
redThings1 = cv2.bitwise_and(img, img, mask=mask2)
cv2.namedWindow("4", 0)
cv2.resizeWindow("4", 600, 600)
cv2.imshow("4",redThings1)


cv2.waitKey(0)