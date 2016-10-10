import numpy as np
import cv2

vidRecord = False
vidModify = False
vidName = 'vid.avi'
dataFolder = '../DATA/'

source = raw_input('Input video (file path) / camera (device num): ')

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

if len(source) == 0:
    source = dataFolder+vidName
elif RepresentsInt(source):
    source = int(source)

#Capture video: #number of device/video file name
cap = cv2.VideoCapture(source)

print cap

# Define the codec (DIVX, XVID, MJPG, X264, WMV1, WMV2)
fourcc = cv2.VideoWriter_fourcc(*'XVID') #or: cv2.VideoWriter_fourcc('X','V','I','D') #Before oCV v3.0: cv2.cv.CV_FOURCC(*'DIVX')

#Create VideoWriter object
out = cv2.VideoWriter(dataFolder+'vid-mod.avi',fourcc, 20.0, (640,480))

if(cap.isOpened()):
    print 'Video loaded!'
    print 'Press R to start/stop recording video.'
    print 'Press M to modify/normal video.'
else:
    print 'Video not loaded!'

while(cap.isOpened()):
    ret, frame = cap.read() # Capture frame-by-frame
   
    if ret == True:    
        # Our operations on the frame come here
        if vidModify:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.flip(frame,0)

        # write the modified frame
        if vidRecord:
            out.write(frame)

        # Display the resulting frame
        cv2.imshow('frame',frame)
    else:
        break  #break at the end of video

    k = cv2.waitKey(25)  #if cv2.waitKey(1) & 0xFF == ord('q'):
    if k == 27:         # wait for ESC key to exit
        break
    elif k == ord('r'): # wait for 'r' key to start/stop recording
        vidRecord = not vidRecord
    elif k == ord('m'): # wait for 'm' key to change frame
        vidModify = not vidModify

# Release everything when finished
cap.release()
out.release()
cv2.destroyAllWindows()
