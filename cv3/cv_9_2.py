"""
这里介绍了一种简单的方法来追踪颜色
并且用红色圆圈标出位置
具体方法：将得到的mask每一行、每一列分别求和，得到两个一维数组
取数组中做小值的索引分别作为横纵坐标，然后在原图中画出红色圆圈
"""
print(__doc__)
import numpy as np
import cv2 as cv
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
	lower_blue = np.array([20,150,50])
	upper_blue = np.array([100,255,255])
	#根据阈值构建掩模
	mask = cv.inRange(hsv,lower_blue,upper_blue)
	#对原图像和掩模进行按位运算（黑：0，白：1）
	res = cv.bitwise_and(frame,frame,mask = mask)
	a = np.sum(np.argsort(np.sum(mask,axis = 0))[-5:-1])//4
	b = np.sum(np.argsort(np.sum(mask,axis = 1))[-5:-1])//4
	#print(a,b)
	#显示图像
	#	cv.imshow('frame',frame)
	#	cv.imshow('mask',mask)
	#cv.imshow('res',res)
	cv.circle(frame,(a,b),40,(0,0,255),3)
	#排除边缘的影响
	if a>2 and b>2:
		#cv.imshow('res',res)
		cv.imshow('frame',frame)
	k = cv.waitKey(5)&0xFF
	if k == 27:
		break
cv.destroyAllWindows()

#print(hsv_green)