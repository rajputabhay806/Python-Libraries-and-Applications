# Lab Sheet 5 - Q15
import cv2
image = cv2.imread("sample.jpg")
if image is None: raise FileNotFoundError("Put sample.jpg beside this script.")
cv2.putText(image, "Simplex - small", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.putText(image, "Complex - larger", (20, 90), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 0, 255), 2)
cv2.putText(image, "Triplex", (20, 140), cv2.FONT_HERSHEY_TRIPLEX, 1.3, (255, 0, 0), 2)
cv2.imshow("Text styles and sizes", image)
cv2.waitKey(0); cv2.destroyAllWindows()
