# -*- coding: utf-8 -*-
import numpy as np
import cv2

def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(img,(x,y),10,(255,0,0,),-1)

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20)&0xFF==27:
        break
cv2.destroyAllWindows()
