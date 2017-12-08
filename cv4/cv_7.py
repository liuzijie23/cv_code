import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
'''
几何变换之图像阈值自适应阈值
参数一：阈值计算方法
	cv.ADAPTIVE_THRESH_MEAN_C:阈值取自相邻阈的平均值
	cv.ADAPTIVE_THRESH_GAUSSIAN_C:阈值取自相邻区域的
	加权值权重为一个高斯窗口
参数二：Block Size 临域大小（计算阈值的区域大小）
参数三：C （最后减去这个常数）
返回值只有一个（图像）
'''
img = cv.imread('cc.jpg',0)

# 中值滤波
img = cv.medianBlur(img,5)

ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)

#11:Block size, 2:C 值
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)

titles = ['Original Image', 'Global Thresholding (v = 127)',
'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']

images = [img, th1, th2, th3]

for i in range(4):
	plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])
plt.show()