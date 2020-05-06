# This function gives the scale factor (mm/px) between the image and the real hand
# Made by Julia Apolonio at 05/05/2020

# Import necessary libraries
import circle

# Function to calculate ratio of real scale(mm/px)
def ratio(path):

	(x,y,r) = circle.crl(path)
	rt = 11.5/r

	return rt

