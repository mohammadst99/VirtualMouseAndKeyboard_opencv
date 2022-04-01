import VirtualKeyboard
import virtualMouse
from VirtualKeyboard import *
from virtualMouse import *
import cv2 as cv
from HandTrackingModule import *

cap =cv.VideoCapture(0)
wCamera =640
hCamera =480
cap.set(3,wCamera)
cap.set(4,hCamera)
sucess , imgShape = cap.read()
wCamera = imgShape.shape[1]
hCamera = imgShape.shape[0]
space = int(hCamera/23)
clickc = 0

def main():
    global clickc
    global space
    global wCamera
    global hCamera
    global cap
    detector = HandDetector
    while True:
        success , img = cap.read()
        img = cv.flip(img , 1)
        imgcopy = img.copy()

        # mouse
        cv.rectangle(img, (space, space), (int(wCamera/2)-space, hCamera-space), (255, 0, 0), cv.FILLED)
        cv.putText(img, "mouse", (int(wCamera/2)-12*space,int(hCamera/2)), cv.FONT_ITALIC, 1, (255, 255, 255), thickness=3)
        # key
        cv.rectangle(img, (int(wCamera/2)+space, space), (wCamera-space, hCamera-space), (255, 0, 0), cv.FILLED)
        cv.putText(img, "keyboard", (int(3*wCamera/4)-3*space, int(hCamera/2)), cv.FONT_ITALIC, 1, (255, 255, 255), thickness=3)


        detector = HandDetector(maxHand=1)
        detector.findhands(imgcopy)
        lmlist, bbox = detector.findPosition(imgcopy)

        if len(lmlist)!=0:
            fingers = detector.fingersUp()
            if fingers[1]==1:
                xIndex , yIndex = lmlist[8][1],lmlist[8][2]

                # keyboard
                if int(wCamera/2)+space < xIndex < wCamera-space and space < yIndex < hCamera-space:
                    cv.rectangle(img, (int(wCamera/2)+space - int(space/5), space - int(space/5)), (wCamera-space + int(space/5), hCamera-space + int(space/5)), (200, 255, 0), cv.FILLED)
                    cv.putText(img, "keyboard", (int(3*wCamera/4)-3*space, int(hCamera/2)), cv.FONT_ITALIC, 1, (255, 255, 255), thickness=3)
                    if fingers[2] == 1:
                        l, b = detector.findDistance(8, 12, imgcopy)
                        if l < 50:
                            clickc = 1
                        if clickc:
                            clickc += 1
                            cv.rectangle(img, (int(wCamera/2)+space - int(space/5), space - int(space/5)), (wCamera-space + int(space/5), hCamera-space + int(space/5)), (0, 255, 0), cv.FILLED)
                            cv.putText(img, "keyboard", (int(3*wCamera/4)-3*space, int(hCamera/2)), cv.FONT_ITALIC, 1, (255, 255, 255), thickness=3)

                        if clickc >= 3 and l > 50:
                            clickc = 0
                            VirtualKeyboard.main()



                # mouse
                if space < xIndex < int(wCamera/2)-space and space < yIndex < hCamera-space:
                    cv.rectangle(img, (space - int(space/5), space - int(space/5)), (int(wCamera/2)-space + int(space/5), hCamera-space + int(space/5)), (200, 255, 0), cv.FILLED)
                    cv.putText(img, "mouse", (int(wCamera/2)-12*space,int(hCamera/2)), cv.FONT_ITALIC, 1, (255, 255, 255), thickness=5)
                    if fingers[2] == 1:
                        l, b = detector.findDistance(8, 12, imgcopy)
                        if l < 50:
                            clickc = 1
                        if clickc:
                            clickc += 1
                            cv.rectangle(img, (space - int(space/5), space - int(space/5)), (int(wCamera/2)-space + int(space/5), hCamera-space + int(space/5)), (0, 255, 0), cv.FILLED)
                            cv.putText(img, "mouse", (int(wCamera/2)-12*space,int(hCamera/2)), cv.FONT_ITALIC, 1, (255, 255, 255), thickness=5)
                        if clickc >= 3 and l > 50:
                            clickc = 0
                            virtualMouse.main()


        imgNew = cv.bitwise_and(img , imgcopy)
        cv.imshow("result", imgNew)
        if cv.waitKey(1) & 0xFF==ord('q'):
            break

if __name__ == "__main__":
    main()