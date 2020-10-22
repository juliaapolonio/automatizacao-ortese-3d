# Algorithm that rotates image based on a contour-fitted line
# To run this code, change to your image path and uncomment desired command lines

import numpy as np
import cv2 as cv
import math 
import imutils


def rot(path):
    # Reads image
    img = cv.imread(path)
    #cv.imshow('palm image',img)
    # To see readen image, uncomment line above

    # Thresholding and blurring image
    hsvim = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lower = np.array([0, 48, 80], dtype = "uint8")
    upper = np.array([20, 255, 255], dtype = "uint8")
    skinRegionHSV = cv.inRange(hsvim, lower, upper)
    blurred = cv.blur(skinRegionHSV, (2,2))
    ret,thresh = cv.threshold(blurred,0,255,cv.THRESH_BINARY)
    #cv.imshow("thresh", thresh)
    # To see result image, uncomment line above

    # Get biggest contour of image
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours = max(contours, key=lambda x: cv.contourArea(x))
    #cv.drawContours(img, [contours], -1, (255,255,0), 2)
    #cv.imshow("contours", img)
    # To see the contour, uncomment lines above

    # Creates a line fitted to contour
    rows,cols = img.shape[:2]
    [vx,vy,x,y] = cv.fitLine(contours, cv.DIST_L2,0,0.01,0.01)
    lefty = int((-x*vy/vx) + y)
    righty = int(((cols-x)*vy/vx)+y)
    #img = cv.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)
    # To see the line, uncomment line above

    # Calculates angle of the line
    angle = abs((cols-1)/(righty-lefty))
    angle = math.degrees(math.atan(angle))

    # Decides which side the rotation will turn
    if angle > 45:
        angle = 180 - angle

    # Rotates image by the angle
    rotated = imutils.rotate_bound(img, angle)

    cv.imwrite(path, rotated)
    #cv.imshow("Rotated (Correct)", rotated)
    #cv.waitKey(0)
    # To see the rotated image or if you uncommented any other line, uncomment lines above

    return
