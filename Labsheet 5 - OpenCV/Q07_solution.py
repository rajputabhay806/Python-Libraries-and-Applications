# Lab Sheet 5 - Q7
import cv2
image = cv2.imread("sample.jpg")
if image is None: raise FileNotFoundError("Put sample.jpg beside this script.")
h, w = image.shape[:2]
cropped = image[h//4:3*h//4, w//4:3*w//4]
cv2.imshow("Center crop", cropped)
cv2.waitKey(0); cv2.destroyAllWindows()
