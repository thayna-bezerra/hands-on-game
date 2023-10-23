import cv2
import mediapipe as mp

video = cv2.VideoCapture(0)

hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = video.read()
    imgRGB = cv2.cv2Color(img, cv2.COLOR_BGR2RGB)
    results = Hand.process(imgRGB)

    cv2.imshow("Hands On Game!", img)
    cv2.waitKey(1)
