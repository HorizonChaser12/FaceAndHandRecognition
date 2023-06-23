import math
import os
import sys
import time
import cv2
import face_recognition
import mediapipe as mp
import numpy as np
import pyautogui
# print("The person does not have access")
cnt = pyautogui.alert('No User found in Frame.To continue press OK!!')
if cnt == "OK":
    pyautogui.alert("Please enter the password to check whether")
    password = pyautogui.password("Enter the password", "BTC", mask='*')
    if password == "BTC":
        os.startfile("E:\HandTracking(HACKLATHON)\Images")
    else:
        pyautogui.alert("The passowrd you entered is wrong.Exiting the program!! :(")
        quit()
