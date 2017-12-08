import numpy as np
import cv2 as cv

img = cv.imread('mm.PNG')

b,g,r = cv.split(img)	#通道分割

k = np.zeros((529,558),np.uint8)	#产生一个图片大小的0矩阵

#合成一幅新的图片，按照（B，G，R）的顺序
img = cv.merge((b,g,k))
cv.imshow('kk',img)		#显示合成后的图片
cv.waitKey(2000)&0xff

img = cv.merge((b,k,r))
cv.imshow('kk',img)
cv.waitKey(2000)&0xff

img = cv.merge((k,g,r))
cv.imshow('kk',img)
cv.waitKey(2000)&0xff

cv.destroyWindow('kk')