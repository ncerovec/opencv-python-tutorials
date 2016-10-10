import numpy as np
import cv2
import matplotlib.pyplot as plt    #from matplotlib import pyplot as plt

imgName = 'img.jpg'
dataFolder = '../DATA/'

#Load an image modes: #1/cv2.IMREAD_COLOR #0/cv2.IMREAD_GRAYSCALE #-1/cv2.IMREAD_UNCHANGED
img = cv2.imread(dataFolder+imgName,1)

#Pixel at coordinates x=100,y=100
px = img[100,100]               #Accessing one pixel
blue = img[100,100,0]           #Accessing only blue of pixel
green = img[100,100,1]          #Accessing only green of pixel
red = img[100,100,2]            #Accessing only red of pixel
img[100,100] = [255,255,255]    #Modify one pixel
print 'Pixel 100x100: ' + str(px), blue, green, red

#Pixel at coordinates x=10,y=10
px = img.item(10,10,2)          #Accessing only red pixel
img.itemset((10,10,2),255)      #Modify red of pixel
print 'Pixel 10x10 - red: ' + str(px)

print 'Image shape (num rows, num columns, num channels): ' + str(img.shape)
print 'Number of pixels: ' + str(img.size)
print 'Number of pixels: ' + str(img.dtype)

#Copy RegionOfImage to another position in image
roi = img[350:390,315:335] #[height-start:height-end,width-start:width-end]
img[350:390,335:355] = roi

#Splitting RGB channels to each of B,G,R colors
b,g,r = cv2.split(img)  #OR:  b = img[:,:,0]
img = cv2.merge((b,g,r))

#Make border/padding - types:
    #cv2.BORDER_CONSTANT
    #cv2.BORDER_REFLECT
    #cv2.BORDER_REPLICATE
    #cv2.BORDER_REFLECT_101
    #cv2.BORDER_DEFAULT
    #cv2.BORDER_REPLICATE
    #cv2.BORDER_WRAP

RED = [255,0,0] #matplotlib: RED <-> BLUE colors / type: cv2.BORDER_CONSTANT
replicate = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()

#Image preview
cv2.imshow('image',img)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite(dataFolder+'img-mod.png',img)
    cv2.destroyAllWindows()
