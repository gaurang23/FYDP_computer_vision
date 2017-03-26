 # import cv2
# import numpy as np
#
# img1 = cv2.imread('1.jpg', 0)
# img2 = cv2.imread('2.jpg', 0)
#
# img1 = cv2.blur(img1, (9, 9))               # normalized block filter
# img2 = cv2.blur(img2, (9, 9))               # normalized block filter
#
# img1 = cv2.resize(img1, None, None, 0.5, 0.5)
# img2 = cv2.resize(img2, None, None, 0.5, 0.5)
#
# ret, thresh = cv2.threshold(img1, 127, 255, 0)
# ret, thresh2 = cv2.threshold(img2, 127, 255, 0)
# i1, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cnt1 = contours[0]
# i2, contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cnt2 = contours[0]
#
# ret = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
# print ret

# TEMPLATE MATCHING

import cv2
import numpy as np

img = cv2.imread('UGB_2.jpg', 0)
img2 = img.copy()
template = cv2.imread('ball2.jpg', 0)
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED',
           'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)

    # Apply template Matching
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img,top_left, bottom_right, 255, 2)

    cv2.imshow("Detected point", img)
    cv2.waitKey(0)
