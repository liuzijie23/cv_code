# -*- coding: utf-8 -*-
import numpy as np
import cv2

img = np.zeros((512,512,3),np.uint8)

cv2.line(img,(0,0),(511,511),(255,0,0),5)

cv2.rectangle(img,(0,0),(512,512),(0,255,0),3)

cv2.circle(img,(256,256),256,(0,0,255),1)

cv2.ellipse(img,(256,256),(256,128),90,0,45,(255,255,0),-1)

pts = np.array([[10,5],[20,30],[70,20],[50,10],[30,90]],np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'opencv',(10,500),font,4,(255,255,255),20)

winname = 'example'
cv2.namedWindow(winname)
cv2.imshow(winname,img)
cv2.waitKey(2000)
cv2.destroyAllWindows()
