# Click code taken from https://stackoverflow.com/questions/32770654/get-pixel-location-using-mouse-click-events/60445099#60445099
# Made by Julia Apolonio at 05/05/2020

# Import necessary libraries
import cv2
import scale_ob
import numpy as np
import time
import math

# Stores each right-click event coordinates [x, y]
right_clicks = list()


# This function will be called whenever the mouse is right-clicked
def img_click(path):

	# Open image
	img = cv2.imread(path,0)

	# Scale image
	scale_width = 640 / img.shape[1]
	scale_height = 480 / img.shape[0]
	scale = min(scale_width, scale_height)
	window_width = int(img.shape[1] * scale)
	window_height = int(img.shape[0] * scale)

	# Rename and resize window according to scale
	cv2.namedWindow('image', cv2.WINDOW_NORMAL)
	cv2.resizeWindow('image', window_width, window_height)

	# Displays the image, gets two right-clicks in that, draw circles at the events and then closes image
	while True:
		# Show image
		cv2.imshow("image", img)
		# Get mouse event
		cv2.setMouseCallback('image', mouse_callback)
		key = cv2.waitKey(1) & 0xFF
		# Draw circles at clicks and then close image
		if len(right_clicks) == 1:
			cv2.circle(img,(right_clicks[0][0],right_clicks[0][1]),10,(255,0,0),-1)
		elif len(right_clicks) == 2:
			cv2.circle(img,(right_clicks[1][0],right_clicks[1][1]),10,(255,0,0),-1)
			cv2.imshow("image", img)
			key = cv2.waitKey(500) & 0xFF
			break

	cv2.destroyAllWindows()

	# Calls real scale ratio function to a variable
	object_scale = scale_ob.ratio(path)

	# Obtains the value of desired coordinates, then calculate horizontal or vertical distance between them

	xa = right_clicks[0][0]
	xb = right_clicks[1][0]
	ya = right_clicks[0][1]
	yb = right_clicks[1][1]
	dp = math.sqrt(pow((xa-xb),2)+pow((ya-yb),2))
	d = dp*object_scale

	# Distance obtained is returned by function
	right_clicks.clear()
	return d

# Mouse callback function
def mouse_callback(event, x, y, flags, params):

    # Right-click event value is 2
    if event == cv2.EVENT_LBUTTONDBLCLK:
    	global right_clicks
    	# Store the coordinates of the right-click event
    	right_clicks.append([x, y])