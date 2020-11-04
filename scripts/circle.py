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

	gaussian = cv2.GaussianBlur(gray, (11, 11), 0) #5 5

	canny = cv2.Canny(gaussian, 40, 100) #100 200

	rows = canny.shape[0]
	circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, 1, rows/8, param1=100, param2=20, minRadius=20, maxRadius=100)

	if circles is not None:
		circles_np = np.uint16(np.around(circles))
		for i in circles_np[0, :]:
			center = (i[0], i[1])
			cv2.circle(output, center, 1, (0, 100, 100), 3)
			radius = i[2]
			cv2.circle(output, center, radius, (255, 0, 255), 3)

	output = cv2.resize(output, (500, 500))
#	cv2.imshow('image', output)
#	cv2.waitKey(0)
#	cv2.destroyAllWindows()

# Return values
	for (x,y,r) in circles[0]:
		return (x,y,r)

#(x,y,r) = crl('../data/images/sevs.jpeg')
