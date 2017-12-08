import numpy as np
import cv2 as cv
'''
几何变换之平移
cv.warpAffine()
参数一：要平移的图像
参数二：平移矩阵
参数三：输出图像大小
'''
#读入一幅图片
img = cv.imread('xx.png')
#print(img.shape)
#(189,199)，查看原图大小，使输出和原来相同,宽高顺序相反
#构造平移矩阵，[[1,0,tx],
#				[0,1,ty]]	数据类型为np.float32
dst = np.array([[1,0,50],[0,1,100]],dtype = np.float32)

res = cv.warpAffine(img,dst,(199,189))

cv.imshow('res',res)
cv.imshow('img',img)
cv.waitKey(5000)

cv.destroyAllWindows()