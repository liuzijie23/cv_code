import numpy as np
import cv2 as cv
'''
这个函数用来观察threshold函数的结果。滑动条回调
函数threshold_hs：首先得到滑动条当前值，再改变阈
值参数，最后得到新的mask。在循环语句中画出mask。
'''

#加载一张图像
img_mask = cv.imread('cc.jpg')

#传回图像的形状，生成一张形状相同的mask
rows,cols,channels = img_mask.shape
mask = img_mask[0:rows,0:cols]

#将原来的图像转换成灰度图
img2gray = cv.cvtColor(img_mask,cv.COLOR_BGR2GRAY)

#回调函数
def threshold_hs(x):
	global mask
	a = cv.getTrackbarPos('number','image')
	ret,mask = cv.threshold(img2gray,a,255,cv.THRESH_BINARY)
	#cv.bitwise_not()用于取反
	#mask = cv.bitwise_not(mask)
#生成一幅图（image），在图中生成滑动条（number）
cv.namedWindow('image')
cv.createTrackbar('number','image',0,255,threshold_hs)

#第一次会显示原图，因为回调函数没有被调用
while(1):
	cv.imshow('image',mask)
	k=cv.waitKey(1)&0xFF
	if k==27:
		break