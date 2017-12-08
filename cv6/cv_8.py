import cv2 as cv
import numpy as np
'''
轮廓近似
采用Douglas-Peucker算法
cv.approxPolyDP()
将原轮廓的形状用更少的点组成新轮廓
参数二（epsilon）：原始轮廓到近似轮廓的最大距离
是一个准度参数
返回一个由轮廓上的点构成的列表
'''
imgx = cv.imread('ww.jpg')
img = cv.imread('ww.jpg',0)
ret,thresh = cv.threshold(img,127,255,0)
ret,contours,hierarchy = cv.findContours(thresh,1,2)

cnt = contours[0]

epsilon = 0.01*cv.arcLength(cnt,True)
#epsilon = 0.1*cv.arcLength(cnt,True)
approx = cv.approxPolyDP(cnt,epsilon,True)

print('epsilon',epsilon)
print('approx',approx)

#画出用来近似轮廓的所有点
for i in range(len(approx)):
	cv.circle(imgx,(approx[i,0,0],approx[i,0,1]),5,(0,255,0),2)

cv.imshow('imgx',imgx)
cv.waitKey(0)