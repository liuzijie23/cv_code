import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
'''
形态学转换之开运算、闭运算、形态学梯度、礼帽、黑帽
开运算：先腐蚀再膨胀
闭运算：先膨胀再腐蚀
形态学梯度：膨胀与腐蚀的差别
礼貌：原图与开运算的差别
黑帽：原图与闭运算的差别
cv.morphologyEx()
'''
img = cv.imread('bb.jpg')
kernel = np.ones((8,8),np.uint8)

opening = cv.morphologyEx(img,cv.MORPH_OPEN,kernel)
closing = cv.morphologyEx(img,cv.MORPH_CLOSE,kernel)
gradient = cv.morphologyEx(img,cv.MORPH_GRADIENT,kernel)
tophat = cv.morphologyEx(img,cv.MORPH_TOPHAT,kernel)
blackhat = cv.morphologyEx(img,cv.MORPH_BLACKHAT,kernel)

cv.imshow('img',img)
cv.imshow('opening',opening)
cv.imshow('closing',closing)
cv.imshow('gradient',gradient)
cv.imshow('tophat',tophat)
cv.imshow('blackhat',blackhat)

cv.waitKey(0)