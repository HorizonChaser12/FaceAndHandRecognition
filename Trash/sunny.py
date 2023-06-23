import cv2
import mediapipe as mp
import math
import os
import sys
import time
import face_recognition
import numpy as np
import winsound
import pyautogui

###########################
# Camera Height, width
############################
wcam, hcam = 640, 480
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

while True:
    success, img = cam.read()
    img = cv2.flip(img, 1)

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

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
            # Recognized Face gets the Hand-recogniton
            # Hand-Landmarks marking, circling, drawing lines, and appending them into a list.
            ##############################
            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks:
                    for id, lm in enumerate(handLms.landmark):
                        h, w, c = img.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        cv2.circle(img, (cx, cy), 3, (255, 0, 255), cv2.FILLED)

                    mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            lmlist = []
            if results.multi_hand_landmarks:
                myHand = results.multi_hand_landmarks[handNo]
                for id, lm in enumerate(myHand.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    xList.append(cx)
                    yList.append(cy)

                    lmlist.append([id, cx, cy])
                    if draw:
                        cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
                xmin, xmax = min(xList), max(xList)
                ymin, ymax = min(yList), max(yList)
                bbox = xmin, ymin, xmax, ymax

                if draw:
                    cv2.rectangle(img, (xmin - 20, ymin - 20), (xmax + 20, ymax + 20), (0, 255, 0), 2)

            if len(lmlist) != 0:
                x1, y1 = lmlist[8][1:]
                x2, y2 = lmlist[12][1:]
                x3, y3 = lmlist[16][1:]
                x4, y4 = lmlist[20][1:]
                x5, y5 = lmlist[4][1:]
            #################################

            ##############################
            # 0 and 1 in tip ids
            ###############################
            if len(lmlist) != 0:
                fingers = []
                for id in range(0, 5):
                    if lmlist[tipIds[id]][2] < lmlist[tipIds[id] - 2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                print(fingers)
                if len(lmlist) != 0:
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

                #############################
                # Gestures
                #############################
                # for ctrl+a (select all)
                if fingers[0] == 1 and fingers[1] == 0 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:

                    # if distance < 20:

                        while t:
                            pyautogui.click(600, 300, duration=1)
                            pyautogui.hotkey('ctrlleft', 'a')
                            t = False
                            winsound.PlaySound("1.wav", winsound.SND_ASYNC)

                # for ctrl+z (undo)
                elif fingers[1] == 0 and fingers[0] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 1:

                    while t:
                        pyautogui.hotkey('ctrlleft', 'z')
                        t = False
                # For Ctrl+v (paste)
                elif fingers[1] == 1 and fingers[0] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 1:

                    while t:
                        pyautogui.hotkey('ctrlleft', 'v')
                        t = False
                # for alt+F4 (closing)
                elif fingers[1] == 1 and fingers[0] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:

                    while t:
                        pyautogui.hotkey('altleft', 'F4')
                        t = False
                elif fingers[1] == 1 and fingers[0] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 0:

                    while t:
                        t = False
                # for resetting/confirming
                if fingers[1] == 0 and fingers[0] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
                    t = True

        ############################

        # re = hands.process(imgRGB)
        # Drawing the circles and connecting the dots on the landmarks
        # imgRGB = detector.findHands(imgRGB)

        ########################
        # Drawing boxes over non-recognized faces
        ########################
        if name == "Not Recognized":
            print("The person does not have access")

        # y1, x2, y2, x1 = faceloc
        # # since we scaled down by 4 times
        # y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
        # cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        # cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
        # cv2.putText(img, name, (x1 + 6, y2 - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

        if name == "Not Recognised":
            print("Exiting the program in 1....2....3.....")
            x = pyautogui.alert(
                title="Program Ended",
                text="The program has finished. Thank you for using it!!",
                button=["Kudos Devs!!", "No.Wait!!"]
            )
            if x == "Kudos Devs!!":
                quit()

        ######################
        # To show FPS and image tab
        ######################
        cTime = time.time()
        fps = 1 / (cTime - ptime)
        ptime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (40, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0), 3)
        cv2.imshow("image", img)
        cv2.waitKey(1)
        #########################

cam.release()
cv2.destroyAllWindows()
