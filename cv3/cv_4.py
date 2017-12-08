import cv2 as cv
import numpy as np

x = np.uint8([250])
y = np.uint8([10])

w = cv.add(x,y)
#250+10 = 260 => 255
print(w)
print(w.shape)
#250+10 = 260 %256 = 4
print(x+y)