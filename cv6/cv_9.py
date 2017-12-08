import cv2 as cv
import numpy as np
'''
凸包：与轮廓近似很像
cv.convexHull(points[,clockwise[,returnPoints]])
参数一（points）：要传入的轮廓
参数二（hull）：输出，通常不需要
参数三：（clockwise）：如果为True，则输出凸包是顺时针方向的
参数四（returnPoints）：若为True，则返回凸包上点的坐标，否则
返回凸包的索引
凸性检验：
cv.isContourConvex(),返回True or False
'''

img = cv.imread('ww.jpg',0)
ret,thresh = cv.threshold(img,127,255,0)
ret,contours,hierarchy = cv.findContours(thresh,1,2)

cnt = contours[0]

#返回凸包上的点的坐标
hull = cv.convexHull(cnt)

#返回凸包的索引
#hull = cv.convexHull(cnt,False,True,False)
#print(hull2)
#[[118]
#[119]
#[121]
#[123]
#[158]

#画出用来凸包上的所有点
for i in range(len(hull)):
	cv.circle(img,(hull[i,0,0],hull[i,0,1]),5,0,2)

#print(cv.isContourConvex(hull))
#True

cv.imshow('img',img)
cv.waitKey(0)