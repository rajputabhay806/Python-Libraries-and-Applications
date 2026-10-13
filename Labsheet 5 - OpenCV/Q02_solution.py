# Lab Sheet 5 - Q2
import cv2
IMAGE_PATH = "sample.jpg"
image = cv2.imread(IMAGE_PATH)
if image is None: raise FileNotFoundError(f"Could not read {IMAGE_PATH}")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Color", image)
cv2.imshow("Grayscale", gray)
cv2.waitKey(0); cv2.destroyAllWindows()
