import numpy as np
import cv2
import matplotlib.pyplot as plt    #from matplotlib import pyplot as plt

imgName = 'img.jpg'
dataFolder = '../DATA/'

#Load an image modes: #1/cv2.IMREAD_COLOR #0/cv2.IMREAD_GRAYSCALE #-1/cv2.IMREAD_UNCHANGED
img = cv2.imread(dataFolder+imgName,0)

print img

#Simple Image preview
cv2.imshow('image',img)

#Advanced Image preview
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite(dataFolder+'img-gray.png',img)
    cv2.destroyAllWindows()
