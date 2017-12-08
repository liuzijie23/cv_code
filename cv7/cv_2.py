import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
'''
'''
img = cv.imread('messi.jpg')
color = ('b','g','r')

# 对一个列表或数组既要遍历索引又要遍历元素时
# 使用内置enumerrate 函数会有更加直接，优美的做法
#enumerate 会将数组或列表组成一个索引序列。
# 使我们再获取索引和索引内容(i,col)的时候更加方便
for i,col in enumerate(color):
	histr = cv.calcHist([img],[i],None,[256],[0,256])
	plt.plot(histr,color = col)
	plt.xlim([0,256])
plt.show()