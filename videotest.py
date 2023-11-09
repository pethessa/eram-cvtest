# install python 3.12.0-amd64
# Update pip (23.3.1)
# python.exe -m pip install --upgrade pip

import cv2

input_video_path = './Input_video1.mp4'
input_video_path = './video2.mov'

cap = cv2.VideoCapture(input_video_path)

def process(ret, image):
    blur = cv2.pyrMeanShiftFiltering(image, 11, 21)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.015 * peri, True)
        if len(approx) == 4:
            x,y,w,h = cv2.boundingRect(approx)
            cv2.rectangle(image,(x,y),(x+w,y+h),(36,255,12),2)
    cv2.imshow('thresh', thresh)
    cv2.imshow('image', image)
    #cv2.waitKey()


while(cap.isOpened()):
    ret, frame = cap.read()
    #print(frame, ret)
    if ret:
        process(ret, frame)
        cv2.imshow("frame", frame)
        cv2.waitKey(1)
    else:
        break

cap.release()
cv2.destroyAllWindows()

