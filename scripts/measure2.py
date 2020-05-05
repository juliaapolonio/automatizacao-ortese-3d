# Part of image processing script
# Made by Julia Apolonio in 24/04/2020
# Feature: gets contourn and hull of hand, but not the convexity deffects
# Works perfectly on Ubuntu with these paths names

# Import necessary libraries
import numpy as np
import cv2

# Read, treat and binarize image
img = cv2.imread('../data/images/gradient.jpeg',1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
ret,thresh = cv2.threshold(blur,50,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Find contours of image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Find hull of all contours
hull = []
for i in range(len(contours)):
    hull.append(cv2.convexHull(contours[i], False))

# Create a new black image
drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)

# Draw contours and hulls
for i in range(len(contours)):
    color_contours = (0, 255, 0) # green - color for contours
    color = (255, 0, 0) # blue - color for convex hull
    cv2.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
    cv2.drawContours(drawing, hull, i, color, 1, 8)

# Show output images
cv2.imshow("title", drawing)
cv2.waitKey()
