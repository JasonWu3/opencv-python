import numpy as np
import time
import cv2
import os

import _thread
cam = 1
send_flag = 0
#close_pixel = 80

def imageprocessing():
    if cam:
        cap = cv2.VideoCapture(0)
        close_pixel = 80
    else:
        cap = cv2.VideoCapture("1.avi")
        close_pixel = 30
    cap.set(3,640)
    cap.set(4,480)
    fgbg = cv2.createBackgroundSubtractorMOG2()
    #fgbg = cv2.createBackgroundSubtractorKNN()
    kernel = np.ones((2,2),np.uint8)
    kernel_d = np.ones((8, 8), np.uint8)
    #white = np.ones((255,255),np.uint8)
    #white = white * 255

    white = np.full((255,255),255)
    print(white.shape)
    cv2.imshow("k", white)
    kernel_close = np.ones((close_pixel, close_pixel), np.uint8)
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.waitKey(0)
    while 1:
        flag = 0
        kong = np.zeros((cap.get(4),cap.get(3),1),np.uint8)
        timenow = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
        timestr = str(time.strftime("%Y-%m-%d_%H;%M;%S", time.localtime()))
        ret, frame = cap.read()
        fgmask = fgbg.apply(frame)
        if cv2.waitKey(1) & 0xff == ord('p'):
            cv2.imwrite(timestr+".png",frame)
            #print("ok")
        f1=cv2.erode(fgmask,kernel, iterations = 1)
        f2=cv2.dilate(f1,kernel, iterations = 1)
        #f3=cv2.morphologyEx(f2,cv2.MORPH_OPEN,kernel)
        ret1,two = cv2.threshold(f2,30,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        image,contours,hierarchy=cv2.findContours(two,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        #print(type(contours))  是list类
        for i in contours:
            if cv2.contourArea(i)>50:
                if flag == 0:
                    sendimage(send_flag)
                    flag=1
                #print(i)
                cv2.drawContours(kong, i,-1, 255, 4)
        #kong = cv2.dilate(kong, kernel_d)
        kong = cv2.morphologyEx(kong,cv2.MORPH_CLOSE,kernel_close)
        image1, contours1, hierarchy1 = cv2.findContours(kong, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours1:
            x,y,w,h=cv2.boundingRect(c)
            if w*h>600 and w/h<6 :
                frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        #cv2.drawContours(frame,contours,-1,(0,0,255),3)
        cv2.putText(frame, 'demo by cooper_wu', (5, 30), font, 0.5, (255, 0, 0), 1)
        #print(timestr)
        #cv2.waitKey(0)
        cv2.putText(frame,timenow ,(5,60),font, 0.5, (0, 0, 255), 1)
        cv2.imshow('frame',kong)
        cv2.imshow('src',frame)
        k = cv2.waitKey(10) & 0xff
        if k == 27:
             break
    cap.release()
    cv2.destroyAllWindows()
def sendimage(saveflag):
        if saveflag == 1:
            print("ok")
            cv2.waitKey(1000)

#main
imageprocessing()