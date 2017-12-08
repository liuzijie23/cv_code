import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
'''
几何变换之仿射变换（原图中平行的线变换后同样平行）
cv.warpAffine()
cv.getAffineTransform()
参数一：第一幅图中的三个点
参数二：第二幅图中的三个点

'''
#读入一幅图片
img = cv.imread('xx.png')

#这里要么传入宽、高，要么导入灰度图
rows,cols = img.shape[:2]

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv.getAffineTransform(pts1,pts2)

dst = cv.warpAffine(img,M,(2*cols,2*rows))

# while(1):
	# cv.imshow('img',dst)
	# cv.imshow('ii',img)
	# if cv.waitKey(5)&0xFF==27:
		# break
# cv.destroyAllWindows()

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Ouput')
plt.show()
