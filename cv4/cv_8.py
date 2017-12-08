import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
'''
Otsu's 二值化
作用：自动寻找图像中的最佳阈值
retVal为返回的最佳阈值
'''

img = cv.imread('cc.jpg',0)

# global thresholding
#全局阈值（127，255）
ret1,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)

# Otsu's thresholding
# Otsu's 阈值
ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

# Otsu's thresholding after Gaussian filtering
#先用（5，5）的高斯核除去噪音
#（5,5）为高斯核的大小，0 为标准差
blur = cv.GaussianBlur(img,(5,5),0)

# 阈值一定要设为0！
ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

# plot all the images and their histograms
images =[img,0,th1,img,0,th2,blur,0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
'Original Noisy Image','Histogram',"Otsu's Thresholding",
'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

# 这里使用了pyplot 中画直方图的方法，plt.hist, 要注意的是它的参数是一维数组
# 所以这里使用了（numpy）ravel 方法，将多维数组转换成一维，也可以使用flatten 方法
#ndarray.flat 1-D iterator over an array.
#ndarray.flatten 1-D array copy of the elements of an array in row-major order.
for i in range(3):
	plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
	plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
	plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
	plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
	plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
	plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()

#print(cv.THRESH_BINARY)
#print(type(cv.THRESH_BINARY))
#0
#<class 'int'>