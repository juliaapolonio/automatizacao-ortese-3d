# Part of image processing script
# Made by Julia Apolonio on 24/04/2020
# Feature: gets coin from image and its radius and x,y center coordinates
# Works perfectly on Ubuntu with these paths names

# Import the necessary packages
import numpy as np
import cv2

# Create the function to be called by other scripts
def crl(path):

# Load the image, clone it for output, and then convert it to grayscale
	image = cv2.imread(path,1)
	output = image.copy()
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect circles in the image
	circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=150, param2=30, minRadius=0, maxRadius=0)
	
# Ensure at least some circles were found
	if circles is not None:
		
# Convert the (x, y) coordinates and radius of the circles to integers
		circles = np.round(circles[0, :]).astype("int")

# Return values
		for (x,y,r) in circles:
			return (x,y,r)
