# -*- coding: utf-8 -*-
import numpy as np
import cv2

#保存一张图像
img = cv2.imread('jj.PNG',cv2.IMREAD_UNCHANGED)
cv2.imshow('image',img)
k = cv2.waitKey(0)&0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('jjjjjjjj.png',img)
    cv2.destroyAllWindows()
