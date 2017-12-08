import numpy as np
import cv2 as cv

from matplotlib import pyplot as plt
BLUE=[255,0,0]

img = cv.imread('mm_3.PNG')

#100,100,100,100:对应top,bottom,left,right
#重复最边上的元素：aaa|abcdefgh|hhhh
replicate = cv.copyMakeBorder(img,100,100,100,100,cv.BORDER_REPLICATE)

#边界元素的镜像：7654|4567|7654
reflect = cv.copyMakeBorder(img,100,100,100,100,cv.BORDER_REFLECT)

#边界元素的镜像*没有最边缘上的）：765|4567|654
reflect101 = cv.copyMakeBorder(img,100,100,100,100,cv.BORDER_REFLECT_101)

#平移后连接：cdefgh|abcdefgh|abcdefg
wrap = cv.copyMakeBorder(img,100,100,100,100,cv.BORDER_WRAP)


#添加常数值参数，还需要一个参数[B，G，R]
constant = cv.copyMakeBorder(img,100,100,100,100,cv.BORDER_CONSTANT,value = BLUE)

plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WARP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()