import cv2
import numpy as np
import matplotlib.pyplot as plt

imgName = 'img.jpg'
dataFolder = '../DATA/'

img = cv2.imread(dataFolder+imgName,0)
img = cv2.medianBlur(img,5)

#Global Tresholding types:
    #cv2.THRESH_BINARY
    #cv2.THRESH_BINARY_INV
    #cv2.THRESH_TRUNC
    #cv2.THRESH_TOZERO
    #cv2.THRESH_TOZERO_INV

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

#Adaptive Tresholding types:
    #cv2.ADAPTIVE_THRESH_MEAN_C
    #cv2.ADAPTIVE_THRESH_GAUSSIAN_C

thresh6 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
thresh7 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

#Otsu's binarization thresholding
    #Automatically calculates a threshold value for bimodal image
    #Bimodal image - Image with two histogram peaks

ret, thresh8 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV', 'ADAP_MEAN', 'ADAP_GAUSS', 'OTSU_BIN']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5, thresh6, thresh7, thresh8]

for i in xrange(9):
    plt.subplot(3,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()


