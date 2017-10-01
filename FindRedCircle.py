import cv2
import numpy as np

debug = 1
font=cv2.FONT_HERSHEY_SIMPLEX
kernel = np.ones((3,3),np.uint8)
src = cv2.imread('1.jpg')
gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
ret,dst1 = cv2.threshold(gray,30,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
#cv2.imshow("dst1",dst1)
dst2 = cv2.morphologyEx(dst1,cv2.MORPH_CLOSE,kernel)
dst2 = cv2.morphologyEx(dst2,cv2.MORPH_OPEN,kernel)
#cv2.imshow("kong",dst2)
image1, contours1, hierarchy1 = cv2.findContours(dst2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours1:
    if cv2.contourArea(cnt)>10:
        x, y, w, h = cv2.boundingRect(cnt)
        src = cv2.rectangle(src,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(src, str(w),(x,y-5) ,font, 0.5, (0, 0, 255), 1)
        cv2.putText(src, str(h), (x-25, int(y+(h/2))), font, 0.5, (0, 0, 255), 1)
        if y+h+20 < src.shape[0]:
            cv2.putText(src, 'area:'+str(w*h), (x, y + h+15), font, 0.5, (0, 0, 255), 1)
        else:
            cv2.putText(src, 'area:'+str(w*h), (x + w + 5 , y + h), font, 0.5, (0, 0, 255), 1)
cv2.imshow("src",src)
cv2.waitKey(0)
#输入图像名称
