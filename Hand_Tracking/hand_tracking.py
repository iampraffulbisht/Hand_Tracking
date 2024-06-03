import cv2 as cv
import  mediapipe as mp
import time
from mediapipe.framework.formats import landmark_pb2
from mediapipe.python.solutions.drawing_utils import DrawingSpec


landmark_drawing_spec = DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)  # Green color for landmarks
connection_drawing_spec = DrawingSpec(color=(0, 255, 0), thickness=2)  # Red color for connections

cap = cv.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

cTime=0
pTime =0


while True:
    success,img = cap.read()

    imgRGB =cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)  ------> tells coordinates or landmarks

    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            for id,lm in enumerate(handlms.landmark):  # lm containes x,y,z coordinates of landmark points
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w),int(lm.y*h)
                print(id,cx,cy)
                if id ==12:
                    cv.circle(img,(cx,cy),15,(255,0,255),cv.FILLED)
                mpDraw.draw_landmarks(img, handlms, mpHands.HAND_CONNECTIONS,landmark_drawing_spec,connection_drawing_spec)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv.putText(img,str(int(fps)),(10,70),cv.FONT_HERSHEY_DUPLEX,3,(20,255,57),3)

    cv.imshow("Image",img)
    cv.waitKey(1)
