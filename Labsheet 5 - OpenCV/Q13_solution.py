# Lab Sheet 5 - Q13
import cv2
import os
SAVE_DIR = "captured_frames"
os.makedirs(SAVE_DIR, exist_ok=True)
camera = cv2.VideoCapture(0)
if not camera.isOpened(): raise RuntimeError("Could not open webcam.")
count = 0
try:
    while count < 100:
        ok, frame = camera.read()
        if not ok: break
        cv2.imshow("Capturing frames - press q to stop", frame)
        cv2.imwrite(os.path.join(SAVE_DIR, f"frame_{count+1:03d}.jpg"), frame)
        count += 1
        if cv2.waitKey(1) & 0xFF == ord("q"): break
finally:
    camera.release()
    cv2.destroyAllWindows()
print(f"Saved {count} frame(s) in {SAVE_DIR}")
