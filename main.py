import cv2 
import numpy as np 
import random
from mypackages import fun

points = []
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
   
if (cap.isOpened()== False):  
  print("Error opening video  file")
ret, frame = cap.read()  
n =  10*int((frame.shape[0]*frame.shape[1])**0.5)

while(cap.isOpened()): 
    m = 0
    ret, frame = cap.read()

    while m < n:
        x = random.randint(0, frame.shape[0]-1)
        y = random.randint(0, frame.shape[1]-1)
        points.extend([[x,y]])
        m += 1
    # print(points)    
    fun.detection(points, frame) 

    if ret == True: 
        
        if len(points) > 1:
            
            while len(points) > 10:
                
                dist = fun.distance(points[0], points)
                dev = fun.deviation(dist, fun.average(dist))
                uni = fun.unify(dist, dev, points)  
                # print(uni)
                aim = tuple(fun.resultant(uni))
                radius = fun.radiation(aim, uni)
                img = cv2.circle(frame, (aim[1],aim[0]), radius, (80, 246, 19), 2)
                done = True
                frame[aim[0] - int(radius/4) : aim[0] + int(radius/4), aim[1] - 1 : aim[1] + 1 ,:] = (80, 246, 19)
                frame[aim[0] - 1 : aim[0] + 1, aim[1] - int(radius/4) : aim[1] + int(radius/4) ,:] = (80, 246, 19)
                dist.clear()
                uni.clear()
                
            points.clear()
        
        
        
        cv2.imshow('Frame', frame) 
        
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break

    else:  
        break
   
cap.release() 

cv2.destroyAllWindows() 
