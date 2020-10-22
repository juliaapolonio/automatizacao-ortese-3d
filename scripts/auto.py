# Find hand keypoints based on a machine learning model
# Algorithm based on https://www.learnopencv.com/hand-keypoint-detection-using-deep-learning-and-opencv/
# To run this code, call function

from __future__ import division
import cv2
import time
import numpy as np
import math

def dist(path):
    protoFile = "../data/models/pose_deploy.prototxt"
    weightsFile = "../data/models/pose_iter_102000.caffemodel"
    nPoints = 22
    POSE_PAIRS = [ [0,1],[1,2],[2,3],[3,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[10,11],[11,12],[0,13],[13,14],[14,15],[15,16],[0,17],[17,18],[18,19],[19,20] ]
    net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

    frame = cv2.imread(path)
    frameCopy = np.copy(frame)
    frameWidth = frame.shape[1]
    frameHeight = frame.shape[0]
    aspect_ratio = frameWidth/frameHeight

    threshold = 0.1

    t = time.time()
    # input image dimensions for the network
    inHeight = 368
    inWidth = int(((aspect_ratio*inHeight)*8)//8)
    inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight), (0, 0, 0), swapRB=False, crop=False)

    net.setInput(inpBlob)

    output = net.forward()
    print("time taken by network : {:.3f}".format(time.time() - t))

    # Empty list to store the detected keypoints
    points = []

    for i in range(nPoints):
        # confidence map of corresponding body's part.
        probMap = output[0, i, :, :]
        probMap = cv2.resize(probMap, (frameWidth, frameHeight))

        # Find global maxima of the probMap.
        minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

        if prob > threshold :
            # Add the point to the list if the probability is greater than the threshold
            points.append((int(point[0]), int(point[1])))
        else :
            points.append(None)

    # Select the desired keypoints
    xah = points [0][0]
    yah = points [0][1]
    xbh = points [12][0]
    ybh = points [12][1]
    xaw = points [5][0]
    yaw = points [5][1]
    xbw = points [17][0]
    ybw = points [17][1]

    inp = [xah, xbh, yah, ybh, xaw, xbw, yaw, ybw]

    return inp
    