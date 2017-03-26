import cv2

# image = cv2.imread("abc.png")
image = cv2.imread("JP_jeep.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# initialize the AKAZE descriptor, then detect keypoints and extract
# local invariant descriptors from the image
detector = cv2.AKAZE_create()
(kps, descs) = detector.detectAndCompute(gray, None)
print("keypoints: {}, descriptors: {}".format(len(kps), descs.shape))

# draw the keypoints and show the output image
cv2.drawKeypoints(image, kps, image, (0, 255, 0))
cv2.imshow("Output", image)
cv2.waitKey(0)