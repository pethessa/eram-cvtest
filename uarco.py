import argparse
import math
import imutils
import cv2
import sys
import pdb

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#pdb.set_trace()

dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
arucoParams = cv2.aruco.DetectorParameters()
arucoDetector = cv2.aruco.ArucoDetector(dictionary, arucoParams)
#(corners, ids, rejected) = cv2.aruco.detectMarkers(image, arucoDict, parameters=arucoParams)


def detectUarco(frame):
    # verify *at least* one ArUco marker was detected
    if len(corners) > 0:
        # flatten the ArUco IDs list
        ids = ids.flatten()
        # loop over the detected ArUCo corners
        for (markerCorner, markerID) in zip(corners, ids):
            # extract the marker corners (which are always returned in
            # top-left, top-right, bottom-right, and bottom-left order)
            corners = markerCorner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = corners
            # convert each of the (x, y)-coordinate pairs to integers
            topRight = (int(topRight[0]), int(topRight[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            topLeft = (int(topLeft[0]), int(topLeft[1]))
            
        # draw the bounding box of the ArUCo detection
        cv2.line(image, topLeft, topRight, (0, 255, 0), 2)
        cv2.line(image, topRight, bottomRight, (0, 255, 0), 2)
        cv2.line(image, bottomRight, bottomLeft, (0, 255, 0), 2)
        cv2.line(image, bottomLeft, topLeft, (0, 255, 0), 2)
        # compute and draw the center (x, y)-coordinates of the ArUco
        # marker
        cX = int((topLeft[0] + bottomRight[0]) / 2.0)
        cY = int((topLeft[1] + bottomRight[1]) / 2.0)
        cv2.circle(image, (cX, cY), 4, (0, 0, 255), -1)
        # draw the ArUco marker ID on the image
        cv2.putText(image, str(markerID),
            (topLeft[0], topLeft[1] - 15), cv2.FONT_HERSHEY_SIMPLEX,
            0.5, (0, 255, 0), 2)
        print("[INFO] ArUco marker ID: {}".format(markerID))
    cv2.imshow("Image", image)
    cv2.waitKey(0)
            

def bounding_box(points):
    x_coordinates, y_coordinates = zip(*points)

    return [(min(x_coordinates), min(y_coordinates)), (max(x_coordinates), max(y_coordinates))]

while(True):
    ret, frame = vc.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res, ids, rejected = cv2.aruco.detectMarkers(gray,dictionary)
    #print(ids)

    minx=1000
    miny=1000
    maxx=0
    maxy=0
    if len(res) > 0:
        cv2.aruco.drawDetectedMarkers(frame,res,ids)
        
    if len(res) > 0:
        try:
            for bbox, id in zip(res, ids):
                #print("BBOX")
                #print(bbox)

                tl = bbox[0][0][0], bbox[0][0][1]
                tr = bbox[0][1][0], bbox[0][1][1]
                br = bbox[0][2][0], bbox[0][2][1]
                bl = bbox[0][3][0], bbox[0][3][1]

            #pdb.set_trace()
            print("RES")
            print(res)
            print(len(res))

            s = [j for i in res for j in i]
            
            r = [j for i in s for j in i]

            #brect = bounding_box(r)
            #print(brect)
            x,y,w,h = cv2.boundingRect(r)#es[0])
            #cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
            cv2.rectangle(frame, brect[0], brect[1], (255, 0, 0), 3)


                # print("TL")
                # print(tl)
                # print("TL0")
                # print(tl[0])
                # #pdb.set_trace()
                # minx=min(minx, tl[0])
                # miny=min(miny, tl[1])
                # maxx=max(maxx, br[0])
                # maxy=max(maxy, br[1])
                # print(minx, miny, maxx, maxy)
                # pdb.set_trace()
                # cv2.line(frame, tl, br, (0, 255, 0), 2)
        except :
            print("eek")
            pass

    # Display the resulting frame
    cv2.imshow('preview',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    #detectUarco(frame)



    #rval, frame = vc.read()
    #key = cv2.waitKey(20)
    #if key == 27: # exit on ESC
    #	break
vc.release()

cv2.destroyWindow("preview")
vc.release()