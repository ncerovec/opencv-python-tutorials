import cv2
import numpy as np

switch = 0
colors = [0,0,0]

def setR(value):
    global colors
    colors[2] = value
    setImageColor()

def setG(value):
    global colors
    colors[1] = value
    setImageColor()

def setB(value):
    global colors
    colors[0] = value
    setImageColor()

def toggleSwitch(value):
    global switch
    switch = value
    setImageColor()

def setImageColor():
    global img, switch, colors    
    if switch == 0:
        img[:] = 0
    else:
        img[:] = colors
    cv2.imshow('image',img)

#Create a black image, a window
img = np.zeros((256,512,3), np.uint8)
cv2.namedWindow('image')

#Create trackbars for color change
cv2.createTrackbar('R','image',0,255,setR)
cv2.createTrackbar('G','image',0,255,setG)
cv2.createTrackbar('B','image',0,255,setB)

#Create switch for ON/OFF functionality
cv2.createTrackbar('0 : OFF \n1 : ON','image',0,1,toggleSwitch)

#Get current positions of four trackbars
#r = cv2.getTrackbarPos('R','image')
#g = cv2.getTrackbarPos('G','image')
#b = cv2.getTrackbarPos('B','image')
#s = cv2.getTrackbarPos(switch,'image')

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
