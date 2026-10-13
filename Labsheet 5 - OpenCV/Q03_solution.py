# Lab Sheet 5 - Q3
import cv2
IMAGE_PATH = "sample.jpg"
image = cv2.imread(IMAGE_PATH)
if image is None: raise FileNotFoundError(f"Could not read {IMAGE_PATH}")
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("RGB channels (displayed by OpenCV)", cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR))
cv2.imshow("HSV representation", hsv)
cv2.waitKey(0); cv2.destroyAllWindows()
