# Lab Sheet 5 - Q10
import cv2
import numpy as np
canvas = np.zeros((400, 600, 3), dtype=np.uint8)
cv2.circle(canvas, (100, 120), 50, (255, 255, 255), 2)
cv2.rectangle(canvas, (220, 70), (340, 170), (255, 255, 255), 2)
triangle = np.array([[450, 170], [500, 70], [550, 170]], dtype=np.int32)
cv2.polylines(canvas, [triangle], True, (255, 255, 255), 2)
gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)
    vertices = len(approx)
    shape = "Triangle" if vertices == 3 else "Rectangle" if vertices == 4 else "Circle" if vertices > 6 else "Unknown"
    print(shape)
cv2.imshow("Shapes", canvas)
cv2.waitKey(0); cv2.destroyAllWindows()
