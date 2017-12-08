# -*- coding: utf-8 -*-
import numpy as np
import cv2

#读入一张图像
img = cv2.imread('jj.PNG',cv2.IMREAD_UNCHANGED)
cv2.imshow('image',img)
cv2.waitKey(0)&0xFF
cv2.destroyWindow('image')
