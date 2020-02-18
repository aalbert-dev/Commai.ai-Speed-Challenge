#!/usr/bin/env python
import numpy
import cv2
import loadnet
from  objecttracker import trackobjects

# get video iterable by frame
vidcap = cv2.VideoCapture('./data/train.mp4')
success, image = vidcap.read()
t = trackobjects(image.shape)

# for each frame
while success:

  # get coordinates of objects in image
  coordinates = loadnet.plot(image)

  # add coordinates to object tracker
  t.add(coordinates)
  
  # report current velocity
  t.report()

  # get next frame
  success, image = vidcap.read()