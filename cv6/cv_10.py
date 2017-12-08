import cv2 as cv
import numpy as np
'''
边界矩形
cv.boundingRect()
x,y,w,h = cv.boundingRect()
分别返回左上角坐标，宽高
'''
imgx = cv.imread('ww.jpg')
img = cv.imread('ww.jpg',0)
ret,thresh = cv.threshold(img,127,255,0)
ret,contours,hierarchy = cv.findContours(thresh,1,2)

cnt = contours[0]
x,y,w,h = cv.boundingRect(cnt)
imgx = cv.rectangle(imgx,(x,y),(x+w,y+h),(0,255,255),2)

cv.imshow('imgx',imgx)
cv.waitKey(0)