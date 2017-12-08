import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
'''
几何变换之图像阈值（全局阈值）
cv.threshold()
参数一：原图像（灰度图）参数二：进行分类的阈值
参数三：高于阈值时赋值  参数四：低于阈值时赋值
阈值方法：
cv.THRESH_BINARY （二值化）  CV.THRESH_BINARY_INV（反向二值化）
CV.THRESH_TRUNC  （截断阈值）CV.THRESH_TOZERO    （超过阈值置零）
CV.TOZERO_INV    （低于阈值置零）
'''
#读入一幅图片
img = cv.imread('bb.jpg',0)

ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img,thresh1,thresh2,thresh3,thresh4,thresh5]

for i in range(6):
	plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])
plt.show()
	

