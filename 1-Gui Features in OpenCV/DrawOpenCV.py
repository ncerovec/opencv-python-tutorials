import numpy as np
import cv2

imgName = 'img-generate.jpg'
dataFolder = '../DATA/'

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)

# Draw a green rectangle with thickness of 3 px
img = cv2.rectangle(img,(384,384),(510,510),(0,255,0),3)

# Draw a red circle filled with color
img = cv2.circle(img,(256,256), 50, (0,0,255), -1)

# Draw a elipse filled with color
img = cv2.ellipse(img,(100,0),(100,50),0,0,180,(255,255,255),-1)

# Draw a polygon
pts = np.array([[20,500],[250,500],[240,510],[10,510]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(255,255,0)) #True/False - closed/open polygon

# Write text with thickness of 3 px
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Nino Cerovec',(25,500), font, 1,(255,255,255),2,cv2.LINE_AA)

print img

cv2.imshow('image',img)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite(dataFolder+imgName,img)
    cv2.destroyAllWindows()
