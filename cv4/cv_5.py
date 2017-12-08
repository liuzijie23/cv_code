import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
'''
几何变换之透视变换（变换后还是直线）
cv.warpPerspective()
cv.getPerspectiveTransform()
参数一：第一幅图中的四个点（任意三个不存在共线）
参数二：第二幅图中的四个点（同上）

'''
#读入一幅图片
img = cv.imread('xx.png')

#这里要么传入宽、高，要么导入灰度图
rows,cols = img.shape[:2]

#构造两个三三不共线的四个点
pts1 = np.float32([[80,20],[120,20],[20,120],[180,120]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

#构造变换矩阵
M = cv.getPerspectiveTransform(pts1,pts2)
#透视变换，可以设置输出大小。
dst = cv.warpPerspective(img,M,(300,300))

#或者用cv里的函数显示
# while(1):
	# cv.imshow('img',dst)
	# cv.imshow('ii',img)
	# if cv.waitKey(5)&0xFF==27:
		# break
# cv.destroyAllWindows()

#用plt可能是便于比较前后的差距
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Ouput')
plt.show()
