# Algorithm that finds the width points on hand by intersection of hand contour and the line
# fitted by two of the ML points.
# To run this, put your image path in the designed variable and uncomment desired commands

import auto
import cv2 as cv
import numpy as np
import math


def cont(path, show_lines = False, show_points = False):

    # Calls ML keypoints function and reads image
    inp = auto.dist(path)
    img = cv.imread(path)

    # Pre-processing: thresholding and blurring image
    hsvim = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lower = np.array([0, 48, 80], dtype = "uint8")
    upper = np.array([20, 255, 255], dtype = "uint8")
    skinRegionHSV = cv.inRange(hsvim, lower, upper)
    blurred = cv.blur(skinRegionHSV, (2,2))
    ret,thresh = cv.threshold(blurred,0,255,cv.THRESH_BINARY)

    # Get biggest contour of image
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours = max(contours, key=lambda x: cv.contourArea(x))

    if show_lines:
        cv.drawContours(img, [contours], -1, (255,255,0), 2)

    if show_points:
        img = cv.circle(img, (inp[4], inp[6]), 2, (255, 0, 0), 2)
        img = cv.circle(img, (inp[5], inp[7]), 2, (255, 0, 0), 2)
        img = cv.circle(img, (inp[1], inp[3]), 2, (0, 0, 255), 2)
        img = cv.circle(img, (inp[0], inp[2]), 2, (0, 0, 255), 2) 

    # Equation of line (normal linear equation)
    def line_eq(X):
        m = (inp[6] - inp[7] ) / (inp[4] - inp[5])
        return m * (X - inp[4]) + inp[6]

    # Creates line with two width points (cv.line creates just a segment)
    line = np.vectorize(line_eq)
    height, width = img.shape[:2]
    img_size = (height, width)
    x = np.arange(0, img_size[0])
    y = line(x).astype('int64')

    if show_lines:
        cv.line(img, (x[0], y[0]), (x[height-1], y[height-1]), (0,0,0))

    # Creates two black images, one with contour and another with line in white
    blank = np.zeros(img.shape[0:2])
    im1 = cv.drawContours(blank.copy(), [contours], 0, 1)
    im2 = cv.line(blank.copy(), (x[0], y[0]), (x[height-1], y[height-1]), 1)

    # Logical bitwise operation to define the intersection between those two images
    intersection = np.logical_and(im1, im2)

    hpoints = []
    aux = []
    wpoints = []

    hpoints += (inp[i] for i in range(4))

    for i in range(height-1):
        for j in range(width-1):
            if intersection[i,j]:
                aux.append(j)
                aux.append(i)

    dist = 0
    for i in range(0,(len(aux)-2),2):
        old_dist = dist
        
        dist = math.sqrt(
                ((aux[i] - aux[i+2]) ** 2) + ((aux[i+1] - aux[i+3]) ** 2)
            )

        if dist > old_dist:
            wpoints = [aux[i], aux[i+1], aux[i+2], aux[i+3]]

    if show_points:
        img = cv.circle(img, (wpoints[0], wpoints[1]), 2, (0, 255, 0), 2)
        img = cv.circle(img, (wpoints[2], wpoints[3]), 2, (0, 255, 0), 2)
    
        img = cv.circle(img, (hpoints[0], hpoints[2]), 2, (0, 255, 0), 2)
        img = cv.circle(img, (hpoints[1], hpoints[3]), 2, (0, 255, 0), 2)

    if show_lines or show_points:
        cv.imshow("foo",img)
        cv.waitKey()

    return hpoints, wpoints
