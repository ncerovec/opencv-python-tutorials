import cv2
import numpy as np
import matplotlib.pyplot as plt

imgName = 'img.jpg'
dataFolder = '../DATA/'

img = cv2.imread(dataFolder+imgName, 0) #read type 1 -> plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

#-> Image Gradients

#Laplacian filter
laplacian = cv2.Laplacian(img,cv2.CV_64F)

#Sobel X filter
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)

#Sobel Y filter
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

#Scharr filter
scharr = cv2.Scharr(img,cv2.CV_64F,0,1)
scharr_sob = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=-1) #ksize=-1: 3x3 Scharr filter - better results

# Output dtype = cv2.CV_8U
sobelx8u = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)

# Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)

titles = ['Original','Laplacian','Sobel X','Sobel Y', 'Scharr', 'Scharr-Sobel', 'Sobel CV_8U', 'Sobel abs(CV_64F)']
images = [img, laplacian, sobelx, sobely, scharr, scharr_sob, sobelx8u, sobel_8u]

plt.axis("off")
for i in xrange(8):
    plt.subplot(2,4,i+1),plt.imshow(images[i],cmap = 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
