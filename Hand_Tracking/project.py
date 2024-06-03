import cv2 as cv
import time
import hand_tracking_module as htm

cTime=0
pTime =0
cap = cv.VideoCapture(0)
detector = htm.handDetector(maxHands=2)
while True:
    success,img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
            print(lmList[4])

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv.putText(img,str(int(fps)),(10,70),cv.FONT_HERSHEY_DUPLEX,3,(20,255,57),3)

    cv.imshow("Image",img)
    cv.waitKey(1)
