# Lab Sheet 5 - Q14
import cv2
import numpy as np
canvas = np.zeros((400, 600, 3), dtype=np.uint8)
cv2.rectangle(canvas, (40, 40), (180, 140), (0, 255, 0), 3)
cv2.circle(canvas, (300, 100), 55, (255, 0, 0), 3)
cv2.line(canvas, (400, 50), (550, 150), (0, 0, 255), 3)
cv2.imshow("Drawing primitives", canvas)
cv2.waitKey(0); cv2.destroyAllWindows()
