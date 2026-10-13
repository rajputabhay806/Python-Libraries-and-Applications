# Lab Sheet 5 - Q4
import cv2
image = cv2.imread("sample.jpg")
if image is None: raise FileNotFoundError("Put sample.jpg beside this script.")
resized = cv2.resize(image, (200, 200))
cv2.imshow("200x200", resized)
cv2.waitKey(0); cv2.destroyAllWindows()
