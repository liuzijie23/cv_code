import numpy as np
import cv2 as cv
'''
几何变换之旋转
cv.warpAffine()
cv.getRotationMatrix2D()
参数一：旋转中心
参数二：旋转角度
参数三：旋转后缩放因子
通过设置旋转中心，缩放因子以及窗口大小来防止旋转后超出边界
'''
#读入一幅图片
img = cv.imread('xx.png')

#这里要么传入宽、高，要么导入灰度图
rows,cols = img.shape[:2]

#获取旋转因子   [ α  , β , (1-α)*center.x-β*center.y ]
#				[ -β , α , β*center.x+(1-α)*center.y ]
#				其中 α = scale*cos(θ),β = scale*sin(θ)
M = cv.getRotationMatrix2D((cols/2,rows/2),45,1)

dst = cv.warpAffine(img,M,(cols,rows))
while(1):
	cv.imshow('img',dst)
	cv.imshow('ii',img)
	if cv.waitKey(5)&0xFF==27:
		break
cv.destroyAllWindows()