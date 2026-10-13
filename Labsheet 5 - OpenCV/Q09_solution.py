# Lab Sheet 5 - Q9
import cv2
image = cv2.imread("sample.jpg")
if image is None: raise FileNotFoundError("Put sample.jpg beside this script.")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cascade_path = cv2.data.haarcascades + "haarcascade_eye.xml"
detector = cv2.CascadeClassifier(cascade_path)
eyes = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(15, 15))
for x, y, w, h in eyes:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
print("Eyes detected:", len(eyes))
cv2.imshow("Eye detection", image)
cv2.waitKey(0); cv2.destroyAllWindows()
