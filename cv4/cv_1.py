import numpy as np
import cv2 as cv
'''
几何变换之扩展缩放
cv.resize()
缩放时推荐使用cv.INTER_AREA
扩展时使用cv.INTER_CUBIC、cv.INTER_LINEAR(默认)
'''
img = cv.imread('xx.png')

#利用缩放因子的方式，所以用 None，再用fx(宽),fy(高)设定放大倍数
res = cv.resize(img,None,fx = 3,fy = 2,interpolation = cv.INTER_CUBIC)

#print(img.shape)
#(189, 199, 3)

#取前两个数，即高和宽,直接设置输出图像大小
#注意：宽、高和传入的顺序不一样
height,width = img.shape[:2]
res = cv.resize(img,(2*width,2*height),interpolation = cv.INTER_CUBIC)

while(1):
	cv.imshow('res',res)
	cv.imshow('img',img)
	if cv.waitKey(1)&0xFF == 27:
		break

cv.destroyAllWindows()
