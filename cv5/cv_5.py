import cv2 as cv
import numpy as np

'''
形态学转换之腐蚀
只有卷积核内全部为前景色，最小元素才为前景色
所以前景色被腐蚀
cv.erode()
参数一：要处理的图像
参数二：卷积核，用numpy生成
参数三：迭代次数
'''
img = cv.imread('bb.jpg')
kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(img,kernel,iterations = 2)

cv.imshow('img',img)
cv.imshow('erosion',erosion)
cv.waitKey(5000)