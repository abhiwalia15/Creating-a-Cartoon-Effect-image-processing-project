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

#convert the blur image into image with edges
grays = cv2.medianBlur(gray, 5)
bluredge = cv2.adaptiveThreshold(grays, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

#getting the blur image
color = cv2.bilateralFilter(img, 9, 300, 300)


################################################################3

#show the original image
cv2.imshow("CARTOONED IMAGE", img)

#show the images with edges
cv2.imshow("Image with Edges", edges)

#show the blurred image
cv2.imshow('Blurred image', blur)

#show the gray image
cv2.imshow('Gray image', gray)

#show the gray image
cv2.imshow('color image', color)


#show the bluredges image
cv2.imshow('bluredge image', bluredge)

cv2.waitKey(0) 
cv2.destroyAllWindows()

