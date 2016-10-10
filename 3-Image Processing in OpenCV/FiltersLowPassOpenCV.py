import cv2
import numpy as np
import matplotlib.pyplot as plt

imgName = 'img.jpg'
dataFolder = '../DATA/'

img = cv2.imread(dataFolder+imgName) #read type 1 -> plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

#-> Smoothing Images

#2D Convolution (Image Filtering)
kernel = np.ones((5,5),np.float32)/25
filter = cv2.filter2D(img,-1,kernel)

#Image Blurring (Image Smoothing)
blur = cv2.blur(img,(5,5))

#Gaussian Filtering
    #create Gaussian kernel - cv2.getGaussianKernel()
gauss = cv2.GaussianBlur(img,(5,5),0)

#Median Filtering
median = cv2.medianBlur(img,5)

#Bilateral Filtering
bilateral = cv2.bilateralFilter(img,9,75,75)

titles = ['Original','Averaging','Blurred','Gaussian', 'Median', 'Bilateral']
images = [img, filter, blur, gauss, median, bilateral]

plt.axis("off")
for i in xrange(6):
    plt.subplot(2,3,i+1),plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
