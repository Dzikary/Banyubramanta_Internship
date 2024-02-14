import cv2
import numpy as np

# trackbar callback function to update HSV value
def callback(x):
    global hsv_low, hsv_high
    hsv_low = np.array([cv2.getTrackbarPos('lowH', 'controls'),
                        cv2.getTrackbarPos('lowS', 'controls'),
                        cv2.getTrackbarPos('lowV', 'controls')])
    hsv_high = np.array([cv2.getTrackbarPos('highH', 'controls'),
                         cv2.getTrackbarPos('highS', 'controls'),
                         cv2.getTrackbarPos('highV', 'controls')])

# create a separate window named 'controls' for trackbars
cv2.namedWindow('controls', cv2.WINDOW_NORMAL)
cv2.resizeWindow("controls", 550, 10)

# create trackbars for high, low HSV values
cv2.createTrackbar('lowH', 'controls', 0, 179, callback)
cv2.createTrackbar('highH', 'controls', 179, 179, callback)
cv2.createTrackbar('lowS', 'controls', 0, 255, callback)
cv2.createTrackbar('highS', 'controls', 255, 255, callback)
cv2.createTrackbar('lowV', 'controls', 0, 255, callback)
cv2.createTrackbar('highV', 'controls', 255, 255, callback)

# initialize HSV low and high values
hsv_low = np.array([20, 20, 20])
hsv_high = np.array([30, 30, 30])

while (1):
    video = cv2.VideoCapture(0)
    success, img = video.read()

    # convert source image to HSV color space
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # apply mask to HSV image based on trackbar positions
    mask = cv2.inRange(image, hsv_low, hsv_high)

    # display images
    cv2.imshow('Mask', mask)
    cv2.imshow('Webcam', img)

cv2.destroyAllWindows()