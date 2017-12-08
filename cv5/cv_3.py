import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
'''
图像平滑之中值模糊：
用卷积框对应像素的中值代替中心像素的值
cv.medianBlur()
参数一：待处理图像
参数二：卷积框大小
'''
img = cv.imread('cc.jpg')

blur = cv.medianBlur(img,5)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('medianBlur')
plt.xticks([]),plt.yticks([])
plt.show()
