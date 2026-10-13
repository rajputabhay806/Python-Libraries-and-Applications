# Lab Sheet 5 - Q5
import cv2
image = cv2.imread("sample.jpg")
if image is None: raise FileNotFoundError("Put sample.jpg beside this script.")
height, width = image.shape[:2]
matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 1.0)
rotated = cv2.warpAffine(image, matrix, (width, height))
cv2.imshow("Rotated 45 degrees", rotated)
cv2.waitKey(0); cv2.destroyAllWindows()
