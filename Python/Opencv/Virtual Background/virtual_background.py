import cv2
import numpy as np
def callback(x):
    pass

cap=cv2.VideoCapture(0)
cv2.namedWindow("image")
cv2.createTrackbar("LH","image",0,255,callback)
cv2.createTrackbar("LS","image",0,255,callback)
cv2.createTrackbar("LV","image",0,255,callback)
cv2.createTrackbar("UH","image",255,255,callback)
cv2.createTrackbar("US","image",255,255,callback)
cv2.createTrackbar("UV","image",255,255,callback)
img=cv2.imread("smarties.png")
while(cap.isOpened()):
    ret,frame=cap.read()
    if (ret==True):
        img=cv2.imread("computer_vision.jpg")
        img=cv2.resize(img,(640,480))
  #  hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        lh=cv2.getTrackbarPos("LH","image")
        ls=cv2.getTrackbarPos("LS","image")
        lv=cv2.getTrackbarPos("LV","image")
        uh=cv2.getTrackbarPos("UH","image")
        us=cv2.getTrackbarPos("US","image")
        uv=cv2.getTrackbarPos("UV","image")
        lb=np.array([lh,ls,lv])
        ub=np.array([uh,us,uv])
        mask=cv2.inRange(frame,lb,ub)
        res=cv2.bitwise_and(frame,frame,mask=mask)
        point=np.where(res==0)
        frame[point]=img[point]
        cv2.imshow("img",img)
        cv2.imshow("res",res)
        cv2.imshow("mask",mask)
        cv2.imshow("frame",frame)
        k=cv2.waitKey(1) & 0xFF
        if k==ord("q"):
            break
cv2.destroyAllWindows()
cap.release()
