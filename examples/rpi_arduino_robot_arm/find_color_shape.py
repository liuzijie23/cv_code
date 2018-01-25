'''
第二问
find(lower,upper,k)
输入颜色对应的阈值和边数
返回中点坐标
'''
import numpy as np
import cv2
import serial

#定义坐标
local = dict(san = [0,0],si = [0,0],yuan = [0,0])
#定义相应颜色对应的阈值范围
lower_red = np.array([0,120,75])
upper_red = np.array([5,255,255])
lower_green = np.array([60,180,50])
upper_green = np.array([90,255,255])
lower_blue = np.array([80,150,100])
upper_blue = np.array([130,255,255])
lower_yellow = np.array([15,180,100])
upper_yellow = np.array([45,255,255])

#定义一个摄像头对象
cap = cv2.VideoCapture(1)
ret,frame_p = cap.read()
#循环检测
	
def find(lower,upper,k):
	#捕获并处理一帧图像
	ret,frame_p = cap.read()
	#高斯滤波后转换到HSV颜色空间
	frame = cv2.medianBlur(frame_p,5)
	frame = cv2.GaussianBlur(frame,(9,9),0)
	
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow('gray',gray)
	mask = cv2.inRange(hsv,lower,upper)
	
	#对原图像和掩模进行按位运算（黑：0，白：1）
	frame = cv2.bitwise_and(frame,frame,mask = mask)
	image,contours,h = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for cnt in contours:
		approx = cv2.approxPolyDP(cnt,0.15*cv2.arcLength(cnt,True),True)
		area = cv2.contourArea(cnt)
		#print(len(approx))
		if (len(approx) == k and area>50):
			#cv2.imshow('img',img)
			img = cv2.drawContours(frame,[cnt],0,(0,255,255),-1)
			M = cv2.moments(cnt)
			cv2.circle(img,(int(M['m10']/M['m00']),int(M['m01']/M['m00'])),40,(0,0,255),3)
		else:
			img = frame
		cv2.imshow('img',img)
		
	#检测圆形
	#gray = cv2.bitwise_and(gray,gray,mask = mask)
	try:
		circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,100,param1=100,param2=30,minRadius=20,maxRadius=100)
		circles = np.uint16(np.around(circles))
		for i in circles[0,:]:
			cv2.circle(frame,(i[0],i[1]),i[2],255,2)
			cv2.circle(frame,(i[0],i[1]),2,255,3)
	except:
		pass
	cv2.imshow('HoughCircles',frame)
	
while(1):
	try:
		#根据传入颜色和边数寻找对应的物体
		find(lower_yellow,upper_yellow,3)
	except:
		pass
	if cv2.waitKey(5)&0xff == 27:
		break

cap.release()
cv2.destroyAllWindows()
