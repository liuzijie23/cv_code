import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
'''
图像平滑之2D卷积
LPF:低通滤波器去除噪声
HPF:高通滤波器用于找到图像边缘
cv.filter2D()
'''
img = cv.imread('xx.png')

kernel = np.ones((5,5),np.float32)/25

dst = cv.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]),plt.yticks([])
plt.show()
