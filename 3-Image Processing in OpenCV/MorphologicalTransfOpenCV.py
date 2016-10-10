import cv2
import numpy as np
import matplotlib.pyplot as plt

imgName = 'img.jpg'
dataFolder = '../DATA/'

img = cv2.imread(dataFolder+imgName,0)

#Structuring Element - Kernels
kernel = np.ones((5,5),np.uint8)
print cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)) #Rectangular Kernel
print cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)) #Elliptical Kernel
print cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5)) #Cross-shaped Kernel

#Erosion (opposite of dilation) - size of foreground object decreases
    #detach two connected objects (removing small white noises)
erosion = cv2.erode(img,kernel,iterations = 1)

#Dilation (opposite of erosion) - size of foreground object increases
    #joining broken parts of object
dilation = cv2.dilate(img,kernel,iterations = 1)

#Opening - Erosion followed by dilation
    #removing noise from and around object
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel) 

#Closing - Dilation followed by Erosion
    #filling holes of object
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

#Morphological Gradient - Difference between dilation and erosion
    #outline of the object
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

#Top Hat - Substraction of Opening from Original
    #remove minorities of object
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

#Black Hat - Substraction of Original from Closing
    #highlight minorities of object
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

titles = ['Original','Erosion','Dilation','Opening', 'Closing', 'Morphological Gradient', 'Top Hat', 'Black Hat']
images = [img, erosion, dilation, opening, closing, gradient, tophat, blackhat]

plt.axis("off")
for i in xrange(8):
    plt.subplot(2,4,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
