# -*- coding: utf-8 -*-
"""
创建滑动条，产生【RGB】颜色
"""
import cv2
import numpy as np
def nothing(x):
	pass
# 创建一副黑色图像
img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')

#创建三个滑动条，范围都是0~255，回掉函数是 nothing
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

#创建一个滑动条，文本为'单引号里的内容'
switch='0:OFF\n1:ON'
cv2.createTrackbar(switch,'image',0,1,nothing)

#循环执行检测操作
while(1):
	cv2.imshow('image',img)		#显示一幅图
	k=cv2.waitKey(1)&0xFF		#判断键盘输入
	if k==27:					#如果是27，即Esc键
		break					#跳出循环
	r=cv2.getTrackbarPos('R','image')	#得到'r'滑动条的值
	g=cv2.getTrackbarPos('G','image')	#。。。
	b=cv2.getTrackbarPos('B','image')	#。。。
	s=cv2.getTrackbarPos(switch,'image')#。。。	
	if s==0:					#如果开关没有开启
		img[:]=0				#显示的img全部为0，即黑色
	else:
		img[:]=[b,g,r]			#开关开启，则显示滑动条颜色

cv2.destroyAllWindows()