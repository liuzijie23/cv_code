import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
'''
轮廓
在二值化图像中查找轮廓：
cv.findContours()
参数一：输入图像
参数二：轮廓检索模式
参数三：轮廓近似方法（cv.CHAIN_APPROX_NONE/SIMPLE）
后者不保存所有值
返回参数一：图像
参数二：Python列表，包含轮廓坐标
参数三：轮廓层析结构

轮廓之绘制轮廓
cv.drawContours()
参数一：图像
单数二：轮廓（Python列表）
参数三：轮廓的索引（用于绘制独立轮廓
若为-1，则绘制所有轮廓）
参数四：颜色
参数五：厚度
'''

img = cv.imread('ww.jpg')
imgray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,thresh = cv.threshold(imgray,127,255,0)
image,contours,hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

#print(type(contours))
#<class 'list'>

#画出所有轮廓
img = cv.drawContours(img,contours,-1,(0,255,0),3)

cv.imshow('thresh',thresh)
cv.imshow('img',img)

cv.waitKey(0)
