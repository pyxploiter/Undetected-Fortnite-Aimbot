# USAGE
# python real_time_object_detection.py --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel
 
# import the necessary packages
import win32api
 
import pygame as pygame
import pythoncom
import win32con
from PIL import ImageGrab
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2
import pyautogui
import random
 
def loadModel():
	prott1 = 'model/MobileNetSSD_deploy.prototxt.txt'
	prott2 = 'model/MobileNetSSD_deploy.caffemodel'
	# load our serialized model from disk
	print("[INFO] loading model...")
	net = cv2.dnn.readNetFromCaffe(prott1, prott2)
	# initialize the list of class labels MobileNet SSD was trained to
	# detect, then generate a set of bounding box colors for each class
	return net;

def play(type):    
	net = loadModel()
	CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
			   "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
			   "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
			   "sofa", "train", "tvmonitor"]
	COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
 
	while True:
		# grab the frame from the threaded video stream and resize it
		# to have a maximum width of 400 pixels
	 
		frame = np.array(ImageGrab.grab(bbox=(0, 40, 1920, 1080)))
		# frame = imutils.resize(frame, width=400)
	 
		# grab the frame dimensions and convert it to a blob
		(h, w) = frame.shape[:2]
		blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
									 0.007843, (300, 300), 127.5)
	 
		# pass the blob through the network and obtain the detections and
		# predictions
		net.setInput(blob)
		detections = net.forward()
	 
		# loop over the detections
		for i in np.arange(0, detections.shape[2]):
			# extract the confidence (i.e., probability) associated with
			# the prediction
			confidence = detections[0, 0, i, 2]
	 
			# filter out weak detections by ensuring the `confidence` is
			# greater than the minimum confidence
			#confidence is 0.6
			if confidence > 0.6:
				# extract the index of the class label from the
				# `detections`, then compute the (x, y)-coordinates of
				# the bounding box for the object
				idx = int(detections[0, 0, i, 1])
				box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
				(startX, startY, endX, endY) = box.astype("int")
	 
				# draw the prediction on the frame
				label = "{}: {:.2f}%".format(CLASSES[idx],
											 confidence * 100)
				cv2.rectangle(frame, (startX, startY), (endX, endY),
							  COLORS[idx], 2)
				y = startY - 15 if startY - 15 > 15 else startY + 15
				cv2.putText(frame, label, (startX, y),
							cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
				if 'person' in label:
					# print ('Detected:',label)
					pygame.init()
					pygame.event.get()
					# if pygame.mouse.get_pressed():
					offsetSX = 510
					offsetEX = 1110
					offsetSY = 400
					offsetEY = 1070
					#tried to detect my character's offset and add the best way to exclude it, failed most tests.
					#can you draw the bounding box of following coordinates?? in between values rakh ra...color fix krdy koi?
					cv2.rectangle(frame, (offsetSX, offsetSY), (offsetEX, offsetEY),(255,255,255), 2)
					midLeft = [startX, (startY+endY)/2]
					midTop =  [(startX+endX)/2,startY]
					midRight = [endX , (startY+endY)/2]
					midBottom = [(startX+endX)/2,endY]
					flag = 0
					if midLeft[0] > offsetSX and midLeft[0] < offsetEX and midLeft[1] > offsetSY and midLeft[1] < offsetEY:
						flag += 1
					if midTop[0] > offsetSX and midTop[0] < offsetEX and midTop[1] > offsetSY and midTop[1] < offsetEY:
						flag += 1
					if midRight[0] > offsetSX and midRight[0] < offsetEX and midRight[1] > offsetSY and midRight[1] < offsetEY:
						flag += 1
					if midBottom[0] > offsetSX and midBottom[0] < offsetEX and midBottom[1] > offsetSY and midBottom[1] < offsetEY:
						flag += 1 
					if flag > 3:                                
						print ('Detected self:',label)                  
						# win32api.SetCursorPos((100, 100))
						# pyautogui.moveTo(100, 100)
						# pygame.mouse.set_pos([100,100])
						# pyautogui.dragTo(100, 100)
						# ctypes.windll.user32.SetCursorPos(100, 100)
					else:
						print ('Detected somebody else:',label)
						# pyautogui.dragTo(1800, 100)
						# pyautogui.moveTo(1800, 100)
						# pygame.mouse.set_pos([1800,1000])
						# ctypes.windll.user32.SetCursorPos(1800, 100)
						nosum = int(round(startX * 1)) + int(round(startX * 0.06))
						nosum2 = int(round(y * 1)) + int(round(y * 0.7))
						halfX = (endX - startX) / 2
						halfY = (endY - startY) / 2
						
						
						if type == "Novice":
							finalX = int(startX + halfX) + random.randint(-150,150)
							finalY = int(startY + halfY) + random.randint(-150,150)
						elif type == "Smart":
							finalX = int(startX + halfX) + random.randint(-50,50)
							finalY = int(startY + halfY) + random.randint(-50,50)
						elif type == "Master":
							finalX = int(startX + halfX)
							finalY = int(startY + halfY)
						win32api.SetCursorPos((finalX, finalY))
						win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, finalX, finalY, 0, 0)
						win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, finalX, finalY, 0, 0)

		# show the output frame
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF
		# if the `q` key was pressed, break from the loop
		if key == ord("q"):
			break
		# update the FPS counter 
	# stop the timer and display FPS information
	# do a bit of cleanup
	cv2.destroyAllWindows()



