import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
'''
结构化元素
用于构建特殊形状的核函数
cv.getStructuringElement()
'''

rect = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
ellipse = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
cross = cv.getStructuringElement(cv.MORPH_CROSS,(5,5))

print(rect,'\n')
print(ellipse,'\n')
print(cross)
