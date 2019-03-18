#import modules
import cv2
import numpy as np

#read the image
img = cv2.imread('abhi.jpg')

# 1)first create the gray scale image and get its blur image with Edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)


# 2)Secondly we will Colorise the image using bilateral filter method
color = cv2.bilateralFilter(img, 9, 300, 300)

# 3)Lastly we will add the color image and the blkwht image with edges 
#   using the bitwise and operator and get our final Cartoon image
cartoon = cv2.bitwise_and(color, color, mask=edges)



#show the result

#show the original image
cv2.imshow("Image", img)

#show the cartoon image
cv2.imshow("Cartoon", cartoon)

#show the color image
cv2.imshow("color", color)

#show the blur image with edges
cv2.imshow("edges", edges)

#terminate the result
cv2.waitKey(0)
cv2.destroyAllWindows()
