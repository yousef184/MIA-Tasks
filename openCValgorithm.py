#can detect only balls

from math import dist
import cv2
import numpy as np


preCircle = None
dist = lambda x1,y1,x2,y2: (x1-x2)**2+(y1-y2)**2
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    if not ret: break

    greyFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurframe = cv2.GaussianBlur(greyFrame,(17,17),0)
    circles = cv2.HoughCircles(blurframe,cv2.HOUGH_GRADIENT,1.2,100,param1=100,param2=30,minRadius=80,maxRadius=200)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        choosen = None
        for i in circles[0,:]:
          choosen=i
          if preCircle is not None:
            if dist(choosen[0],choosen[1],preCircle[0],preCircle[1]) <= dist(i[0],i[1],preCircle[0],preCircle[1]):
                choosen = i
        cv2.circle(frame,(choosen[0],choosen[1]),1,(0,100,100),3)
        cv2.circle(frame,(choosen[0],choosen[1]),choosen[2],(255,0,255),3)           
        preCircle = choosen

    cv2.imshow("circles",frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
