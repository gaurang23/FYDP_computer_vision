import cv2
import numpy as np

green_min = np.uint8([[[255, 255, 255]]])
hsv_green = cv2.cvtColor(green_min, cv2.COLOR_BGR2HSV)
print "hsv_green = {0}".format(hsv_green)
greenLower = np.uint8([[[29, 86, 6]]])
greenUpper = np.uint8([[[64, 255, 255]]])
bgr_lower = cv2.cvtColor(greenLower, cv2.COLOR_HSV2BGR)
bgr_upper = cv2.cvtColor(greenUpper, cv2.COLOR_HSV2BGR)
print "bgr_lower = {0}".format(bgr_lower)
print "bgr_upper = {0}".format(bgr_upper)
