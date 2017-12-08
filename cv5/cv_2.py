import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
'''
图像平滑之高斯模糊：
cv.GaussianBlur()
返回处理后的图像
自己构建高斯核函数：
cv.getGaussianKernel()
返回一个呈高斯分布的数组，
'''
img = cv.imread('cc.jpg')
#blur_1 = cv.getGaussianKernel(5,10)
#blur_2 = cv.getGaussianKernel(5,10)
#print(blur_1)
#[[ 0.19205063]
# [ 0.20392638]
# [ 0.20804597]
# [ 0.20392638]
# [ 0.19205063]]

blur = cv.GaussianBlur(img,(7,7),0)
##重复几次模糊操作
# blur = cv.GaussianBlur(blur,(7,7),0)
# blur = cv.GaussianBlur(blur,(7,7),0)
# blur = cv.GaussianBlur(blur,(7,7),0)
# blur = cv.GaussianBlur(blur,(7,7),0)
# blur = cv.GaussianBlur(blur,(7,7),0)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('GaussianBlur')
plt.xticks([]),plt.yticks([])
plt.show()
