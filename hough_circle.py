import cv2
import numpy as np

# read image
# image = cv2.imread("1.jpg")
image = cv2.imread("2.jpg")
# image = cv2.imread("UGB_1.jpg")
# image = cv2.imread("UGB_2.jpg")

# smoothing/noise removal - remove if UGB_1 or UGB_2
# image = cv2.blur(image, (9, 9))               # normalized block filter
image = cv2.GaussianBlur(image, (9, 9), 2)    # gaussian filter
# image = cv2.medianBlur(image, 15)             # median filter
# image = cv2.bilateralFilter(image, 20, 5, 5)    # bilateral filter

# resize - don't if UGB_2
image = cv2.resize(image, None, None, 0.5, 0.5)
output = image.copy()

# change image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# circle detection using Hough transforms
# circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 0.5, 120)      # for 1
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 0.5, 1)      # for 2
# circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 0.5, 120)      # for UGB_1
# circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 80)       # for UGB_2

# ensure at least some circles were found
if circles is not None:
    # convert the (x, y) coordinates and radius of the circles to integers
    circles = np.round(circles[0, :]).astype("int")

    # loop over the (x, y) coordinates and radius of the circles
    for (x, y, r) in circles:
        # draw the circle in the output image, then draw a dot at the center of the circle
        cv2.circle(output, (x, y), r, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.circle(output, (x, y), 3, (0, 0, 255), -1, cv2.LINE_AA)

    # show the output image
    cv2.imshow("output", np.hstack([image, output]))
    cv2.waitKey(0)
else:
    print "No circles found"
