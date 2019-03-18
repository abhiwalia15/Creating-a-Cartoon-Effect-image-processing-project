# Creating-a-Cartoon-Effect-image-processing-project
We’re going to see in this video how to create a cartoon effect using OpenCV and python.

We’re going to see in this video how to create a cartoon effect.
A cartoon has 2 important charateristics:

  * Really clear edges
  * Homogeneus colours
  
Starting from an original image taken with a camera we’re going to give to it a cartoon effect keeping in mind these 2 charateristics.

 In the past few years, image cartoonizer-software has been used for converting the normal image into a cartoon image. In this process, an edge detection and bilateral filter are required. The bilateral filter is used to reduce the color palette of an image. Afterward, we can apply edge detection to this image for generating a dark shaped image. Therefore, finally, some tricks can apply for this image to get a cartoon image.
