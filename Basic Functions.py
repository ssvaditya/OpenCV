import cv2 as cv
import numpy as np
img = cv.imread("images/keanu.png")  # reading the image
kernel = np.ones((2,2))   # 2x2 matrix of ones
# height = 400
# width = 820
# img = cv.resize(img, (width,height))   #resizing image

imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  #Converting RBG image to Grayscale
imgBlur =  cv.GaussianBlur(imgGray, (11,11), 0)     #kernel size should always be odd
imgCanny = cv.Canny(img, 200, 200)                  #Detects lines in the image
imgDilation = cv.dilate(imgCanny, kernel, iterations = 1)       #Makes lines thicker
imgErosion = cv.erode(imgDilation, kernel, iterations = 1)      #Makes lines thinner

cv.imshow("Gray Image", imgGray)        #GrayImage
cv.imshow("Blurred Image", imgBlur)     #Blurred Image
cv.imshow("Canny Image", imgCanny)      #Canny Image
cv.imshow("Dilated Image", imgDilation)    #Dilated Image
cv.imshow("Eroded Image", imgErosion)   #Eroded Image
cv.waitKey(0)