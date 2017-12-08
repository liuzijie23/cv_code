import cv2 as cv
import numpy as np
'''
轮廓特征之矩
cv.moments()
得到图像的矩，以字典形式返回
矩可以应用在计算图像质心、面积等
'''
imgx = cv.imread('ww.jpg')
img = cv.imread('ww.jpg',0)
ret,thresh = cv.threshold(img,127,255,0)
img2,contours,hierarchy = cv.findContours(thresh,1,2)

cnt = contours[0]
M = cv.moments(cnt)
#print(M)
#print(type(M))
#<class 'dict'>

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

cv.circle(imgx,(cx,cy),5,(0,0,255),2)
cv.imshow('img',imgx)
cv.imshow('img2',img2)

cv.waitKey(0)
#print((cx,cy))
#(375, 246)