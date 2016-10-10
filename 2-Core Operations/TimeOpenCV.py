import numpy as np
import cv2
import time

imgName = 'img.jpg'
dataFolder = '../DATA/'
img = cv2.imread(dataFolder+imgName,1)

f = cv2.getTickFrequency()  #Frequency of clock-cycles (clock-cycles-num/second)

enableOpt = raw_input('Use optimization (yes/no): ')

if (enableOpt == 'yes'):
    cv2.setUseOptimized(True)
else:
    cv2.setUseOptimized(False)

print "Optimization: " + str(cv2.useOptimized())    #Optimization setting

e1 = cv2.getTickCount() #Number of clock-cycles when execution started
t1 = time.time() #Time when execution started

#Functions - mesuring execution time
for i in xrange(5,49,2):
    img1 = cv2.medianBlur(img,i)
print "NumZero: " + str(np.count_nonzero(img))

e2 = cv2.getTickCount() #Number of clock-cycles when execution ended
t2 = time.time() #Time when execution ended

time = (e2-e1)/f   #Time of execution in seconds
print "Time: (" + str(e2) + "-" + str(e1) + ")" + "/" + str(f) + " = " + str(time)

time = (t2-t1) #Time of execution in seconds
print "Time: " + str(t2) + "-" + str(t1) + " = " + str(time)

cv2.imshow('image',img)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite(dataFolder+'img-time.png',img)
    cv2.destroyAllWindows()
