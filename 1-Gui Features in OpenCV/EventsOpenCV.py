import cv2
import numpy as np

imgName = 'img-draw.jpg'
dataFolder = '../DATA/'

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

#Print list of all available events 
events = [i for i in dir(cv2) if 'EVENT' in i]
print events

# mouse callback function
def draw(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDBLCLK:
        if mode == True:
            cv2.rectangle(img,(x-10,y-10),(x+10,y+10),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),20,(255,0,0),-1)

    elif event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(255,255,255),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(255,255,255),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')    #necessary naming window for event environment
cv2.setMouseCallback('image',draw)   #window of event, callback function

while(1):
    cv2.imshow('image',img)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite(dataFolder+imgName,img)
        break
    elif k == 27:
        break

cv2.destroyAllWindows()
