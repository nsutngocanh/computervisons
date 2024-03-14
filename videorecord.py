import cv2
import numpy as np

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

recording = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if recording:
        out.write(frame)
        cv2.circle(frame, (50, 50), 20, (0, 0, 255), -1)

    cv2.imshow('Video Recorder', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord(' '):
        recording = not recording
    elif key == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
