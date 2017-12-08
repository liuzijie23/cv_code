import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
'''
直方图的计算与绘制
直方图概念：
BINS：每一个小组（用histSize表示）
DIMS：收集参数的数目（只收集灰度值则为1）
RANGE：统计灰度值的范围
cv.calcHsit(images,channels,mask,histSize,ranges[,hist[,accumulate]])
1.image:原图像（格式为uint8或float32,用[]括起来）
2.channel:如果输入为彩色图，可选参数为0，1，2（B，G，R）用[]括起来
3.mask:设为None则统计整幅图
4.histSize:BIN数目，用[]括起来
5.ranges:像素范围（通常为[0,256]，用[]括起来）
np.histogram()

'''

img = cv.imread('ww.jpg',0)

#hist是一个256x1的数组
hist = cv.calcHist([img],[0],None,[256],[0,256])

#用numpy里的函数
hist2,bins = np.histogram(img.ravel(),256,[0,256])
print(hist,'\n',hist2'\n',bins)

plt.hist(img.ravel(),256,[0,256])
plt.show()