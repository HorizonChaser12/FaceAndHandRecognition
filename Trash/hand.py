import math
import time

import cv2
import mediapipe as mp

###########################
# Camera Height,width
############################
wcam, hcam = 420, 420
handNo = 0
draw = True
tipIds = [4, 8, 12, 16, 20]

xList = []
yList = []
bbox = []
############################
####################################
# Camera capture and hand recognition
############################
cam = cv2.VideoCapture(0)
cam.set(3, wcam)
cam.set(4, hcam)
ptime = 0

# detector=HandDetector(detectionCon=0.8)
mpHands = mp.solutions.hands

hands = mpHands.Hands(static_image_mode=False,
                      max_num_hands=1,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils
############################


#########################
# adding circles on landmarks and processing rgb
#########################
while True:
    success, img = cam.read()
    img = cv2.flip(img, 1)

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # if id ==0:
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
            # print(lmlist,bbox)

            if len(lmlist) != 0:
                x1, y1 = lmlist[8][1:]
                x2, y2 = lmlist[12][1:]
                x3, y3 = lmlist[16][1:]
                x4, y4 = lmlist[20][1:]
                x5, y5 = lmlist[4][1:]
                # print(x1,y1,x2,y2)

            if len(lmlist) != 0:
                fingers = []
                for id in range(0, 5):
                    if lmlist[tipIds[id]][2] < lmlist[tipIds[id] - 2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                # print(fingers)
                if len(lmlist) != 0:
                    x1, y1 = lmlist[4][1], lmlist[4][2]
                    x2, y2 = lmlist[8][1], lmlist[8][2]
                    x3, y3 = lmlist[12][1], lmlist[12][2]
                    ca1, ca2 = (x1 + x2) // 2, (y1 + y2) // 2
                    cv2.circle(imgRGB, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                    cv2.circle(imgRGB, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
                    cv2.line(imgRGB, (x1, x2), (x2, y2), (255, 0, 255), 3)
                    cv2.circle(imgRGB, (ca1, ca2), 15, (255, 0, 255), cv2.FILLED)
                    length = math.hypot(x2 - x1, y2 - y1)
                    length2 = math.hypot(x3 - x2, y3 - y2)
                    # print(length)
            ######################
            # To show Fps and image tab
            ######################
            cTime = time.time()
            fps = 1 / (cTime - ptime)
            ptime = cTime
            cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("image", img)
    cv2.waitKey(1)
######################
