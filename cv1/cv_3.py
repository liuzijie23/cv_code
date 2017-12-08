# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

img = cv2.imread('jj.PNG',0)
plt.imshow(img,cmap = 'gray',interpolation = 'bicubic')
plt.xticks([]),plt.yticks([])   #去除x、y轴标签值
plt.show()
