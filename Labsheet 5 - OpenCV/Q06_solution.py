# Lab Sheet 5 - Q6
import cv2
image = cv2.imread("sample.jpg")
if image is None: raise FileNotFoundError("Put sample.jpg beside this script.")
cv2.imshow("Horizontal flip", cv2.flip(image, 1))
cv2.imshow("Vertical flip", cv2.flip(image, 0))
cv2.imshow("Both axes", cv2.flip(image, -1))
cv2.waitKey(0); cv2.destroyAllWindows()
