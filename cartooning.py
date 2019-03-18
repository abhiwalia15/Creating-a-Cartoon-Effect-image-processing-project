import cv2
import numpy as np

#read theimage
img = cv2.imread('abhi.jpg')

#threshold of gray scale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#checking out the edges
edges = cv2.Canny(img, 75, 150)

#checking the blurred image, the more we increase the blur ;lesser edges we will get
blur = cv2.medianBlur(img, 7)




################################################################3

#show the original image
cv2.imshow("CARTOONED IMAGE", img)

#show the images with edges
cv2.imshow("Image with Edges", edges)

#show the blurred image
cv2.imshow('Blurred image', blur)

#show the gray image
cv2.imshow('Gray image', gray)


cv2.waitKey(0) 
cv2.destroyAllWindows()

