import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
'''
图像金字塔
cv.pyrUp()
cv.pyrDown()
高斯金字塔：顶部图像中的每个像素值等于下一层图像中5个像素的高斯加权平均
拉普拉斯金字塔：Li=Gi-PyrUp(Gi+1)
'''

img=cv.imread('messi.jpg')

lower_reso = cv.pyrDown(img)
higher_reso2 = cv.pyrUp(img)
#放大缩小前后图像大小可能产生变化
#如果图像size是奇数，会增加一条像素

laplace = cv.subtract(img,cv.pyrUp(lower_reso))

cv.imshow('img',img)
cv.imshow('lower_reso',lower_reso)
cv.imshow('higher_reso2',higher_reso2)
cv.imshow('laplace',laplace)

cv.waitKey(0)
