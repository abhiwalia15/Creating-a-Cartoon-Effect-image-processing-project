import cv2
import numpy as np

#read theimage
img = cv2.imread('Test Images/abhi.jpg')

#checking out the edges
edges = cv2.Canny(img, 75, 150)

#show the original image
cv2.imshow("CARTOONED IMAGE", img)

#show the images with edges
cv2.imshow("Image with Edges", edges)


cv2.waitKey(0)
cv2.destroyAllWindows()

