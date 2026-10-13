# Lab Sheet 5 - Q1
import cv2
IMAGE_PATH = "sample.jpg"
image = cv2.imread(IMAGE_PATH)
if image is None:
    raise FileNotFoundError(f"Could not read {IMAGE_PATH}. Put an image beside this script or update IMAGE_PATH.")
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
