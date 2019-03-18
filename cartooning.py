import cv2
import numpy as np

#read theimage
img = cv2.imread('abhi.jpg')

#check the image
cv2.imshow('CARTOONED IMAGE", img)
cv2.waitkey(0)
cv2.destroyAllWindows()

