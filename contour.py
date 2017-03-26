import cv2
import numpy as np

# read image
# image = cv2.imread("1.jpg")
# image = cv2.imread("2.jpg")
image = cv2.imread("UGB_1.jpg")
# image = cv2.imread("UGB_2.jpg")

# resize
image = cv2.resize(image, None, None, 0.5, 0.5)
output = image.copy()

# change image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)[1]

# smoothing
# gray = cv2.blur(gray, (9, 9))               # normalized block filter
# gray = cv2.GaussianBlur(gray, (9, 9), 2)    # gaussian filter
gray = cv2.medianBlur(gray, 15)             # median filter
# gray = cv2.bilateralFilter(gray, 20, 5, 5)    # bilateral filter

# contours
ret, thresh = cv2.threshold(gray, 127, 255, 0)
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(output, contours, -1, (0, 255, 0), 2)
cv2.imshow("output", np.hstack([image, output]))
cv2.waitKey(0)
