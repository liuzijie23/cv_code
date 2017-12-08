import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
'''
图像平滑之双边滤波：
能保持边界清晰，去除高频噪声，但是速度慢
因为它考虑了大小和相邻点相似性两方面
cv.bilateralFilter()
参数一：待处理图像
参数二：领域直径（卷积框大小）
参数三：空间高斯函数标准差
参数四：灰度值相似性高斯函数标准差
'''
img = cv.imread('bb.jpg')

blur = cv.bilateralFilter(img,9,60,60)
for i in range(50):
	blur = cv.bilateralFilter(blur,9,60,60)

cv.imshow('img',img)
cv.imshow('blur',blur)
# plt.subplot(121),plt.imshow(img),plt.title('Original')
# plt.xticks([]),plt.yticks([])
# plt.subplot(122),plt.imshow(blur),plt.title('bilateralFilter')
# plt.xticks([]),plt.yticks([])
# plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
