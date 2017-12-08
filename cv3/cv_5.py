import cv2 as cv
import numpy as np

img_1 = cv.imread('mm.PNG')
img_2 = cv.imread('jj.PNG')

#cv.addWeighted()需要输入图片具有同样的shape
#图片1占0.7，图片2占0.3
dst = cv.addWeighted(img_1[0:400,0:400],0.7,img_2[0:400,0:400],0.3,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyWindow('dst')
#图片1占0.2，图片2占0.8
dst = cv.addWeighted(img_1[0:400,0:400],0.2,img_2[0:400,0:400],0.8,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyWindow('dst')