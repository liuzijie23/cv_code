import cv2 as cv
import numpy as np
'''
矩的其他应用
cv.contourArea()
或使用M['m00']
得到轮廓的面积
cv.arcLength()
得到轮廓周长
参数二：True表示轮廓是闭合的
'''

img = cv.imread('ww.jpg',0)
ret,thresh = cv.threshold(img,127,255,0)
img2,contours,hierarchy = cv.findContours(thresh,1,2)

cnt = contours[0]

M = cv.moments(cnt)
print('    M[\'m00\']  方式: ',M['m00'],'\n')

area = cv.contourArea(cnt)
print('cv.contourArea方式：',area)

perimeter = cv.arcLength(cnt,True)
print('周长: ',perimeter)