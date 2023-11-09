# install python 3.12.0-amd64
# Update pip (23.3.1)
# python.exe -m pip install --upgrade pip

import cv2

input_video_path = './Input_video1.mp4'

cap = cv2.VideoCapture(input_video_path)

while(cap.isOpened()):
    ret, frame = cap.read()
    print(frame, ret)
    if ret:
        cv2.imshow("frame", frame)
        cv2.waitKey(1)
    else:
        break

cap.release()
cv2.destroyAllWindows()
