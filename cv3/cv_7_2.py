import numpy as np
import cv2 as cv

img = cv.imread('cc.jpg')

e1 = cv.getTickCount()
#此处原代码为：
#for i in xrange(5,49,2):
#新版本xrange和range合并了
for i in range(5,49,2):
	#中值模糊
	img = cv.medianBlur(img,i)
	cv.imshow('haha',img)
	cv.waitKey(100)
e2 = cv.getTickCount()
time = (e2-e1)/cv.getTickFrequency()

print(time)