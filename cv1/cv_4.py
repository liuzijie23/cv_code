# -*- coding: utf-8 -*-
import numpy as np
import cv2
            
cap = cv2.VideoCapture(0)        #笔记本默认是0
#cap.set(3,1920)
#cap.set(4,1080)
while (True):
    ret,frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1)&0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
