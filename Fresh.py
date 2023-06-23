import cv2
import mediapipe as mp
import math
import os
import sys
import face_recognition
import numpy as np
import time
###########################
# Camera Height,width
############################
wcam, hcam = 320, 240  # Lower resolution
handNo = 0
draw = True
tipIds = [4, 8, 12, 16, 20]
t = True
images = []
classNames = []
decide = bool
xList = []
yList = []
bbox = []
############################
# Appends the images into a list
###########################
path = "G:\HandTracking(HACKLATHON)\Images"
mylist = os.listdir(path)
print(mylist)
for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


###########################

###########################
# Finds face encodings and appends it into a list
###########################
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        try:
            encoded_face = face_recognition.face_encodings(img)[0]
        except IndexError as e:
            print(e)
            sys.exit(1)
        encodeList.append(encoded_face)
    return encodeList


encoded_face_train = findEncodings(images)

###########################
# Camera capture and HandDetector
############################
cam = cv2.VideoCapture(0)
cam.set(3, wcam)
cam.set(4, hcam)
ptime = 0
mpHands = mp.solutions.hands

hands = mpHands.Hands(static_image_mode=False,
                      max_num_hands=1,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils


############################

def process_hand_tracking(results, img):
    #########################
    # Color Conversion and Compares the encoding of faces
    #########################
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    faces_in_frame = face_recognition.face_locations(imgS)
    encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)
    for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
        matches = face_recognition.compare_faces(encoded_face_train, encode_face)
        name = "Not Recognized"
        faceDist = face_recognition.face_distance(encoded_face_train, encode_face)
        matchIndex = np.argmin(faceDist)
        print(matchIndex)
        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            ##############################

            ##############################
            # Recognised Face gets the Hand-recogniton
            # Hand-Landmarks marking,circling,drawing lines and appending it into a list.
            ##############################
            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks:
                    for id, lm in enumerate(handLms.landmark):
                        h, w, c = img.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        cv2.circle(img, (cx, cy), 3, (255, 0, 255), cv2.FILLED)

                    mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
                    lmList = []
                    if len(handLms.landmark) != 0:
                        for id, lm in enumerate(handLms.landmark):
                            h, w, c = img.shape
                            cx, cy = int(lm.x * w), int(lm.y * h)
                            lmList.append([id, cx, cy])
                            if len(lmList) != 0:
                                xList.append(lmList[id][1])
                                yList.append(lmList[id][2])
                    x1, y1 = xList[1], yList[1]
                    x2, y2 = xList[4], yList[4]
                    bbox = (x1 - 20, y1 - 20, x2 + 20, y2 + 20)

                    if draw:
                        cv2.rectangle(img, (bbox[0] - 20, bbox[1] - 20),
                                      (bbox[2] + 20, bbox[3] + 20), (0, 255, 0), 2)
                        cv2.putText(img, 'GESTURE CONTROL', (bbox[0] - 20, bbox[1] - 50),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

                    handNo = len(results.multi_hand_landmarks)
                    if handNo == 1:
                        handType = "ONE"
                    elif handNo == 2:
                        handType = "TWO"
                    else:
                        handType = ""
                    cv2.putText(img, f'Hand: {handType}', (10, 70),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    if x1 < bbox[0] or y1 < bbox[1] or x2 > bbox[2] or y2 > bbox[3]:
                        cv2.putText(img, 'HAND OUT OF RANGE', (bbox[0] - 20, bbox[1] - 100),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

                    for id in range(1, 21):
                        if id in tipIds:
                            continue
                        else:
                            cv2.line(img, (xList[id - 1], yList[id - 1]), (xList[id], yList[id]), (0, 255, 0), 2)
                            cv2.circle(img, (xList[id - 1], yList[id - 1]), 3, (0, 0, 255), cv2.FILLED)

            #########################
            # Distance Calculation
            #########################
            try:
                if len(xList) != 0:
                    distance1 = math.sqrt((xList[4] - xList[8]) ** 2 + (yList[4] - yList[8]) ** 2)
                    distance2 = math.sqrt((xList[8] - xList[12]) ** 2 + (yList[8] - yList[12]) ** 2)
                    distance3 = math.sqrt((xList[12] - xList[16]) ** 2 + (yList[12] - yList[16]) ** 2)
                    distance4 = math.sqrt((xList[16] - xList[20]) ** 2 + (yList[16] - yList[20]) ** 2)
                    distance5 = math.sqrt((xList[4] - xList[20]) ** 2 + (yList[4] - yList[20]) ** 2)
                    distance6 = math.sqrt((xList[8] - xList[20]) ** 2 + (yList[8] - yList[20]) ** 2)
                    distance7 = math.sqrt((xList[12] - xList[20]) ** 2 + (yList[12] - yList[20]) ** 2)
                    distance8 = math.sqrt((xList[16] - xList[20]) ** 2 + (yList[16] - yList[20]) ** 2)
                    if distance1 < 40:
                        if distance2 < 40:
                            if distance3 < 40:
                                if distance4 < 40:
                                    if distance5 < 40:
                                        if distance6 < 40:
                                            if distance7 < 40:
                                                if distance8 < 40:
                                                    cv2.putText(img, 'DISTANCE OK', (bbox[0] - 20, bbox[1] - 150),
                                                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                                                else:
                                                    cv2.putText(img, 'MOVE HANDS FURTHER APART',
                                                                (bbox[0] - 20, bbox[1] - 150),
                                                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                                            else:
                                                cv2.putText(img, 'MOVE HANDS FURTHER APART',
                                                            (bbox[0] - 20, bbox[1] - 150),
                                                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                                        else:
                                            cv2.putText(img, 'MOVE HANDS FURTHER APART', (bbox[0] - 20, bbox[1] - 150),
                                                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                                    else:
                                        cv2.putText(img, 'MOVE HANDS FURTHER APART', (bbox[0] - 20, bbox[1] - 150),
                                                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                                else:
                                    cv2.putText(img, 'MOVE HANDS FURTHER APART', (bbox[0] - 20, bbox[1] - 150),
                                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                            else:
                                cv2.putText(img, 'MOVE HANDS FURTHER APART', (bbox[0] - 20, bbox[1] - 150),
                                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                        else:
                            cv2.putText(img, 'MOVE HANDS FURTHER APART', (bbox[0] - 20, bbox[1] - 150),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                    else:
                        cv2.putText(img, 'MOVE HANDS FURTHER APART', (bbox[0] - 20, bbox[1] - 150),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            except IndexError as e:
                print(e)
                sys.exit

