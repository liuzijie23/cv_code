import numpy as np
import cv2 as cv
'''
这里介绍了一种简单的方法来追踪颜色
'''
#用[[[0,255,0]]]因为：这里的三层括号分别应对于
#cvArray、cvMat、IplImage
green = np.uint8([[[0,255,0]]])
hsv_green = cv.cvtColor(green,cv.COLOR_BGR2HSV)

cap = cv.VideoCapture(0)

while(1):
	#捕获一帧数据
	ret,frame = cap.read()
	#转换到HSV颜色空间
	hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
	#设定蓝色阈值
	lower_blue = np.array([20,150,150])
	upper_blue = np.array([100,255,255])
	#根据阈值构建掩模
	mask = cv.inRange(hsv,lower_blue,upper_blue)
	#对原图像和掩模进行按位运算（黑：0，白：1）
	res = cv.bitwise_and(frame,frame,mask = mask)
	#显示图像
	cv.imshow('frame',frame)
	cv.imshow('mask',mask)
	cv.imshow('res',res)
	k = cv.waitKey(5)&0xFF
	if k == 27:
		break
cv.destroyAllWindows()

print(hsv_green)