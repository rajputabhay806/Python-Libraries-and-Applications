# Lab Sheet 5 - Q8
import cv2
image = cv2.imread("sample.jpg")
if image is None: raise FileNotFoundError("Put sample.jpg beside this script.")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
detector = cv2.CascadeClassifier(cascade_path)
faces = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
for x, y, w, h in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
print("Faces detected:", len(faces))
cv2.imshow("Face detection", image)
cv2.waitKey(0); cv2.destroyAllWindows()
