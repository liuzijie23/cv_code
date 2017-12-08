import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
'''
Canny边缘检测
1、去除噪声（高斯滤波器）
2、计算图像梯度（Sobel计算水平与竖直方向的图像梯度Gx，Gy，再计算
Edge_Gradient(G)=sqrt(Gx2+Gy2),Angle(θ)=arctan(Gx/Gy)）
3、非极大值抑制（得到一个“窄边界”二值图像）
4、滞后阈值（设定阈值确定真正的边界）
cv.Canny()
参数一：输入图像
参数二：minVal
参数三：maxVal
参数四：Sobel卷积核大小（）默认是3
参数五：L2gradient（如果设为True,
则用Edge_Gradient(G)=abs(Gx2)+abs(Gy2),默认False）
'''

img=cv.imread('aa.jpg',0)
edges = cv.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edges Image'), plt.xticks([]), plt.yticks([])

plt.show()
