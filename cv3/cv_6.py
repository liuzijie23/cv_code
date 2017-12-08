import numpy as np
import cv2 as cv
#加载图像
img_1 = cv.imread('mm.PNG')
img_2 = cv.imread('jj.PNG')

#传回第二幅图的形状，统一两幅图的形状
rows,cols,channels = img_2.shape
roi = img_1[0:rows,0:cols]

#生成一个掩码（蒙板）
img2gray = cv.cvtColor(img_2,cv.COLOR_BGR2GRAY)
ret,mask = cv.threshold(img2gray,175,255,cv.THRESH_BINARY)
#cv.bitwise_not()用于取反
mask_inv = cv.bitwise_not(mask)

img_1bg = cv.bitwise_and(roi,roi,mask = mask)

img_2fg = cv.bitwise_and(img_2,img_2,mask = mask_inv)

dst = cv.add(img_1bg,img_2fg)
img_1[0:rows,0:cols] = dst

cv.imshow('res',img_1)
cv.imshow('res_0',img2gray)
cv.imshow('res_1',mask)
cv.imshow('res_2',mask_inv)
cv.waitKey(0)
cv.destroyAllWindows()