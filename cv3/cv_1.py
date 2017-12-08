import numpy as np
import cv2 as cv

img = cv.imread('jj.PNG')

print(img.shape)#返回形状，可以判断是灰色图像还是彩色
print(img.size) #返回大小（像素数目）
print(img.dtype)#返回数据类型
#(752, 1337, 3)，（高度，宽度，通道数）
#3016272
#uint8

eyes = img[300:400,700:800]#（纵坐标范围，横坐标范围）
img[500:600,700:800] = eyes#覆盖原图像
cv.imshow('kk',img)
cv.waitKey(0)&0xff
cv.destroyWindow('kk')