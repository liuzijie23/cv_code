'''
检测四种颜色，返回坐标
'''
#导入所需的库
import numpy as np
import cv2 as cv
import serial
import time

#定义坐标
local = [0,0]
#定义相应颜色对应的阈值范围
lower_red = np.array([0,180,100])
upper_red = np.array([10,255,255])
lower_green = np.array([60,150,50])
upper_green = np.array([90,255,255])
lower_blue = np.array([95,100,50])
upper_blue = np.array([125,255,255])
lower_yellow = np.array([15,180,100])
upper_yellow = np.array([45,255,255])

#定义一个摄像头对象
cap = cv.VideoCapture(0)
ser = serial.Serial('/dev/ttyUSB1',9600)
#循环检测
def yanse(lower,upper):
	#捕获一帧数据
	for i in range(7):
		ret,frame = cap.read()
		#高斯滤波后转换到HSV颜色空间
		frame = cv.GaussianBlur(frame,(9,9),0)
		hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
		mask = cv.inRange(hsv,lower,upper)
		#对原图像和掩模进行按位运算（黑：0，白：1）
		res = cv.bitwise_and(frame,frame,mask = mask)
		#计算得到新的坐标，先加6倍再除以10减少抖动
		local[0] = (np.sum(np.argsort(np.sum(mask,axis = 0))[-5:-1])+1*local[0])//5
		local[1] = (np.sum(np.argsort(np.sum(mask,axis = 1))[-5:-1])+1*local[1])//5
	#print(local)
	angle = 1000 + np.around(np.degrees(np.angle(np.complex(local[0]-320,450-local[1]))))
	print(angle)
	#
	cv.circle(frame,(local[0],local[1]),40,(0,0,255),3)
	cv.circle(frame,(320,450),3,(0,0,255),3)
	cv.imshow('frame',frame)
	cv.waitKey(1000)
	ser.write(("a2090").encode())
	time.sleep(2)
	ser.write(("a%d" %angle).encode())
	time.sleep(1)
	ser.write(("a%d" %angle).encode())
	time.sleep(1)
	ser.write(("a2160").encode())
	time.sleep(0.5)
	ser.write(("a4040").encode())
	time.sleep(1)
	ser.write(("a2170").encode())
	time.sleep(1)
	ser.write(("a4005").encode())
	time.sleep(1)
	ser.write(("a2090").encode())
	time.sleep(1)
	
while 1 :
	try:
		yanse(lower_red,upper_red)
		ser.write(("a1022").encode())
		time.sleep(2)
		ser.write(("a2020").encode())
		time.sleep(1)
		ser.write(("a4030").encode())
		time.sleep(1)
		ser.write(("a2090").encode())
		time.sleep(1)
	except:
		pass
	try:
		yanse(lower_green,upper_green)
		ser.write(("a1067").encode())
		time.sleep(2)
		ser.write(("a2020").encode())
		time.sleep(1)
		ser.write(("a4030").encode())
		time.sleep(1)
		ser.write(("a2090").encode())
		time.sleep(1)
	except:
		pass
	try:
		yanse(lower_blue,upper_blue)
		ser.write(("a1112").encode())
		time.sleep(2)
		ser.write(("a2020").encode())
		time.sleep(1)
		ser.write(("a4030").encode())
		time.sleep(1)
		ser.write(("a2090").encode())
		time.sleep(1)
	except:
		pass
	try:
		yanse(lower_yellow,upper_yellow)
		ser.write(("a1157").encode())
		time.sleep(2)
		ser.write(("a2020").encode())
		time.sleep(1)
		ser.write(("a4030").encode())
		time.sleep(1)
		ser.write(("a2090").encode())
		time.sleep(1)
	except:
		pass
	if cv.waitKey(500)&0xff == 27:
		break
cap.release()
cv.destroyAllWindows()
