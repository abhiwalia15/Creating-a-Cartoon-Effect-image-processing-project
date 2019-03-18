import cv2
import numpy as np

#read theimage
img = cv2.imread('Test Images/abhi.jpg')

#checking out the edges
edges = cv2.Canny(img, 75, 150)

#checking the blurred image
blur = cv2.medianBlur(img, 5)







################################################################3

#show the original image
cv2.imshow("CARTOONED IMAGE", img)

#show the images with edges
cv2.imshow("Image with Edges", edges)

#show the blurred image
cv2.imshow('Blurred image', blur)

cv2.waitKey(0) 
cv2.destroyAllWindows()

