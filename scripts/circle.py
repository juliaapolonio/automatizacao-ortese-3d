#Part of image processing script
#Made by Julia Apolonio in 24/04/2020
#Feature: gets coin from image and its radius and x,y center coordinates
#Works perfectly on Ubuntu with these paths names

# Import the necessary packages
import numpy as np
import cv2

# Load the image, clone it for output, and then convert it to grayscale
image = cv2.imread('../data/images/gradient3.jpeg',1)
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect circles in the image
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
# Ensure at least some circles were found
if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv2.circle(output, (x, y), r, (0, 255, 0), 4)
		cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
		print(r)
	
	# Show the output image
	cv2.imshow("output", np.hstack([image, output]))
	cv2.waitKey(0)
