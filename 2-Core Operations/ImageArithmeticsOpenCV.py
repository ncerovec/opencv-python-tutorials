import numpy as np
import cv2
import matplotlib.pyplot as plt    #from matplotlib import pyplot as plt

x = np.uint8([250])
y = np.uint8([10])

imgName1 = 'img.jpg'
imgName2 = 'open-cv.jpg'
imgName3 = 'open-cv.png'
dataFolder = '../DATA/'

#Adding scalar values
print cv2.add(x,y) # 250+10 = 260 => 255
print x+y          # 250+10 = 260 % 256 = 4

#Load images modes: #1/cv2.IMREAD_COLOR #0/cv2.IMREAD_GRAYSCALE #-1/cv2.IMREAD_UNCHANGED
img1 = cv2.imread(dataFolder+imgName1,1)
img2 = cv2.imread(dataFolder+imgName2,1)
img3 = cv2.imread(dataFolder+imgName3,1)

def addBitwise(img, sticker):
    #Create a ROI
    rows,cols,channels = sticker.shape
    roi = img[0:rows, 0:cols]

    #Now create a mask of logo and create its inverse mask also
    stickerGray = cv2.cvtColor(sticker,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(stickerGray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    #Now black-out the area of logo in ROI
    img_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

    #Take only region of logo from logo image.
    sticker_fg = cv2.bitwise_and(sticker,sticker,mask = mask)

    #Put logo in ROI and modify the main image
    result = cv2.add(img_bg,sticker_fg)
    img[0:rows, 0:cols] = result
    return img

#Adding images bitwise
#img1 = addBitwise(img1, img3)

#Adding images by weight
dst = cv2.addWeighted(img1,0.7,img2,0.3,0)

#Image preview
cv2.imshow('image',dst)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite(dataFolder+'img-add.png',dst)
    cv2.destroyAllWindows()
