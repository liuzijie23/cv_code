import numpy as np
import cv2 as cv
'''
颜色空间的转换，在cv中有超过150种,常用的有 BGR<-->Gray,BGR<-->HSV
cv.cvtColor(input_image,flag)
flag:	cv.COLOR_BGR2GRAY,cv.COLOR_BGR3HSV
注意：各个软件HSV格式不一定相同，要注意归一化
'''

#cv.COLOR_BGR2GRAY和cv.COLOR_RGB2GRAY的转换结果不相同！
img = cv.imread('cc.jpg')
img_1 = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('1',img_1)
#z = cv.countNonZero(img)
img_2 = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
cv.imshow('2',img_2)

#打印出所有的转换方式（flag）
flags = [i for i in dir(cv) if i.startswith('COLOR_')]
print(flags)
cv.waitKey(5000)
cv.destroyAllWindows()
