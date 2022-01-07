import cv2 as cv
import numpy as np

#READ IMAGE
img = cv.imread('images/keanu.png')
cv.imshow('Keanu', img)

cv.waitKey(0)              #waitKey takes argument of delay in milli-seconds

#READ VIDEO
frameHeight = 480
frameWidth = 640

cap = cv.VideoCapture("images/test_vid.mp4")
while True:
    success, img = cap.read()
    img = cv.resize(img, (frameWidth, frameHeight))
    cv.imshow("Result", img)
    if cv.waitKey(1) & 0xFF == ord('q'):   #pressing q closes the stream
        break



#READ WEBCAM
cap_webcam = cv.VideoCapture(0)
cap_webcam.set(3, 640)     #height
cap_webcam.set(4, 480)     #width
cap_webcam.set(10, 100)    #brightness

while True:
    success, img = cap_webcam.read()     #success is a boolean which shows if it exists or not
    cv.imshow("Result", img)
    if cv.waitKey(1) & 0xFF == ord('q'):   #pressing q closes the stream
        break