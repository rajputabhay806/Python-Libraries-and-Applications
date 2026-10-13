# Lab Sheet 5 - Q12
import cv2
camera = cv2.VideoCapture(0)
if not camera.isOpened(): raise RuntimeError("Could not open webcam.")
try:
    while True:
        ok, frame = camera.read()
        if not ok: break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Live grayscale - press q to quit", gray)
        if cv2.waitKey(1) & 0xFF == ord("q"): break
finally:
    camera.release()
    cv2.destroyAllWindows()
