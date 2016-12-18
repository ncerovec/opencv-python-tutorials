import numpy as np
import cv2

imgName = 'img.jpg'
dataFolder = '../DATA/'

#-> Image Colorspace
img = cv2.imread(dataFolder+imgName,1)  #open Image

#Colorspace type change flags
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print "Colorspace type change flags: " + str(flags)

#Conversion - types: cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2HSV...
hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('image',hsvImg)

#-> Video Colorspace
cap = cv2.VideoCapture(0)   #capture Camera

#Find HSV color range
color = np.uint8([[[0,255,0 ]]])    #BGR of desired color
hsv_color = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
print "HSV color: " + str(hsv_color)  #Take [H-10,100,100] and [H+10,255,255] for color-range

while(cap.isOpened()):
    ret, frame = cap.read() #Capture frame-by-frame (return 2 values: true/false->ret / value->frame)

    if(ret):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Convert BGR to HSV

        #Define range of blue color in HSV
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])
        lower_green = np.array([50,50,50])
        upper_green = np.array([70,255,255])
        lower_red = np.array([0,50,50])
        upper_red = np.array([10,255,255])

        #Threshold the HSV image to get only certain colors
        maskBlue = cv2.inRange(hsv, lower_blue, upper_blue)
        maskGreen = cv2.inRange(hsv, lower_green, upper_blue)
        maskRed = cv2.inRange(hsv, lower_red, upper_red)

        #Bitwise-AND mask and original image
        resBlue = cv2.bitwise_and(frame,frame,mask=maskBlue)
        resGreen = cv2.bitwise_and(frame,frame,mask=maskGreen)
        resRed = cv2.bitwise_and(frame,frame,mask=maskRed)

        res = cv2.bitwise_or(resBlue,resGreen)
        res = cv2.bitwise_or(res,resRed)

        #cv2.imshow('blue-mask',resBlue)
        #cv2.imshow('green-mask',resGreen)
        #cv2.imshow('red-mask',resRed)
        cv2.imshow('frame',res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
