import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
'''
形态学转换之膨胀
cv.dilate()
'''
img = cv.imread('bb.jpg')
kernel = np.ones((5,5),np.uint8)
dilation = cv.dilate(img,kernel,iterations = 2)

cv.imshow('img',img)
cv.imshow('dilation',dilation)
cv.waitKey(5000)
