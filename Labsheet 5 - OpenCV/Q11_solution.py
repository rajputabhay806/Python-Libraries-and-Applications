# Lab Sheet 5 - Q11
import cv2
camera = cv2.VideoCapture(0)
if not camera.isOpened(): raise RuntimeError("Could not open webcam.")
try:
    while True:
        ok, frame = camera.read()
        if not ok: break
        cv2.imshow("Webcam - press q to quit", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"): break
finally:
    camera.release()
    cv2.destroyAllWindows()
