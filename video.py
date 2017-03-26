import numpy as np
import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    cap.open()

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


# import numpy as np
# import cv2
#
# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)
#
# # Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480), True)
#
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret == True:
#         frame = cv2.flip(frame,0)
#         print frame
#
#         # write the flipped frame
#         out.write(frame)
#
#         cv2.imshow('frame',frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#         else:
#             break
#
# # Release everything if job is finished
# cap.release()
# out.release()
# cv2.destroyAllWindows()