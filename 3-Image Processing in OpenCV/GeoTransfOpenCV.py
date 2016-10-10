import cv2
import numpy as np

imgName = 'img.jpg'
dataFolder = '../DATA/'

img = cv2.imread(dataFolder+imgName,0)

#Transform - RESIZE, TRANSLATE, ROTATE, AFFINE

#Resize - Interpolation methods:
    #zooming: cv2.INTER_CUBIC (slow), cv2.INTER_LINEAR
    #shrinking: cv2.INTER_AREA

#Resize (zoom/strech) image with scale of 2 (width & height)
img = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

#Resize (shrink) image with scale of 1/3 (width & height) - given dimensions
height, width = img.shape[:2]   #get height and width of image
img = cv2.resize(img,(width/3, height/3), interpolation = cv2.INTER_AREA)

rows, cols = img.shape #get rows and cols of image - output image size

#Translation of image as object
M = np.float32([[1,0,30],[0,1,60]]) #transformation matrix
img = cv2.warpAffine(img,M,(cols,rows))

#Rotation of image as object
M = cv2.getRotationMatrix2D((cols/2,rows/2),30,1)
img = cv2.warpAffine(img,M,(cols,rows))

#Affine transformation of image as object - perspective transform
    #Define transformation matrix: 3 points input image -> 3 points output image
pts1 = np.float32([[cols*0.2,rows/2],[cols/2,rows*0.2],[cols,rows]])
pts2 = np.float32([[0,rows/2],[cols/2,0],[cols*0.8,rows*0.8]])
M = cv2.getAffineTransform(pts1,pts2)
img = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('image',img)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite(dataFolder+'img-transform.png',img)
    cv2.destroyAllWindows()
