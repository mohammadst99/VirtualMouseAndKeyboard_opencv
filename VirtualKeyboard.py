
import cv2 as cv

import baseMain
from HandTrackingModule import *
from pynput.keyboard import Controller
from baseMain import *


cap = cv.VideoCapture(0)
wCam = 640
hCam = 480
cap.set(3,wCam)
cap.set(4,hCam)
suc , imageTest = cap.read()
wCam = imageTest.shape[1]
hCam = imageTest.shape[0]
frameR = int(wCam/10)
wTotal = wCam - 2*(frameR) #10key + 9 space = wTotal
size = int(wCam / 16)
space = int((wTotal - 10*size)/10)

capsX=0
capsX1=0
capsY=0
capsY1=0
enterX=0
enterX1=0
enterY=0
enterY1=0
exitX=0
exitX1=0
exitY=0
exitY1=0



click =0
caps = True
close = False

keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]
keysLOW = [["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
        ["a", "s", "d", "f", "g", "h", "j", "k", "l", ";"],
        ["z", "x", "c", "v", "b", "n", "m", ",", ".", "/"]]




class KEY:
    def __init__(self,pos,size,text):
        self.pos = pos
        self.text = text
        self.size = size

def keyClass(keys):
    global size
    global space
    Buttons = []
    for row in range(len(keys)):
        y1 = frameR +((row)*(size+space))
        for i, keyALPHA in enumerate(keys[row]):
            x1=frameR +((i)*(size+space))
            Buttons.append(KEY([x1,y1],[x1+size,y1+size],keyALPHA))

    return Buttons

def DrawKey(img1 , buttons1):
    global capsX
    global capsX1
    global capsY
    global capsY1
    global enterX
    global enterX1
    global enterY
    global enterY1
    global exitX
    global exitX1
    global exitY
    global exitY1

    for button1 in buttons1:
        x,y = button1.pos
        key2 = button1.text
        w,h = button1.size
        cv.rectangle(img1, (x,y), (w,h), (255, 0, 0), cv.FILLED)
        cv.putText(img1,key2,(x+int((size/2)-(size/4)),y+int((size/2)+(size/4))),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),thickness=4)

    cv.rectangle(img1,(frameR-int(size/6),frameR-int(size/6)),(frameR +((10)*(size+space)+int(size/6)-space),frameR +((3)*(size+space)-space)+int(size/6)),(20,60,70),thickness=2)
    # capslock
    cv.rectangle(img1, (capsX:=frameR, capsY:=frameR +((3)*(size+space))+int(size/2)), (capsX1:=frameR+4*size,capsY1:= frameR +((3)*(size+space)+size)+int(size/2)), (255, 0, 0), cv.FILLED)
    cv.putText(img1,"caps lock", (frameR +int(size/6),frameR +((3)*(size+space))+int(size)+int(size/5)),cv.FONT_ITALIC,1 , (255,255,255),thickness=3)
    # space
    cv.rectangle(img1, (enterX:=frameR+ 4*size + 2*space,enterY:=frameR + ((3) * (size + space)) + int(size / 2)),(enterX1:=frameR + 8 * size+2*space,enterY1:= frameR + ((3) * (size + space) + size) + int(size / 2)), (255, 0, 0), cv.FILLED)
    cv.putText(img1, "Space", (frameR +4*size + 4*space+ int(size / 6), frameR + ((3) * (size + space)) + int(size) + int(size / 5)),cv.FONT_ITALIC, 1, (255, 255, 255), thickness=3)

    # exit
    cv.rectangle(img1, (exitX:=frameR+ 8*size + 4*space, exitY:=frameR + ((3) * (size + space)) + int(size / 2)),(exitX1:=frameR + 11 * size+4*space,exitY1:= frameR + ((3) * (size + space) + size) + int(size / 2)), (255, 0, 0), cv.FILLED)
    cv.putText(img1, "Exit", (frameR +8*size + 4*space+ int(size/2)+int(space), frameR + ((3) * (size + space)) + int(size) + int(size / 5)),cv.FONT_ITALIC, 1, (255, 255, 255), thickness=3)

    return img1

def KeyBoard(img , buttonsUP , buttonsLOW):
    keyboard = Controller()
    global close
    global click
    global caps
    imgCoppy = img.copy()
    if caps :
        imgKEY = DrawKey(img,buttonsUP)
        buttons = buttonsUP

    else:
        imgKEY = DrawKey(img, buttonsLOW)
        buttons = buttonsLOW

    detector = HandDetector(maxHand=1)
    detector.findhands(imgCoppy)
    lmlist , bbox = detector.findPosition(imgCoppy)


    img3 = cv.bitwise_and(imgKEY, imgCoppy)

    # finding index position
    if len(lmlist)!=0:
        fingers = detector.fingersUp()
        if fingers[1]==1:
            xIndex , yIndex = lmlist[8][1],lmlist[8][2]

            # space
            if enterX < xIndex < enterX1 and enterY < yIndex < enterY1:
                cv.rectangle(img3, (enterX, enterY), (enterX1, enterY1 + 5), (200, 255, 0), cv.FILLED)
                cv.putText(img3, "Space", (frameR +4*size + 4*space+ int(size / 6), frameR + ((3) * (size + space)) + int(size) + int(size / 5)),cv.FONT_ITALIC, 1, (255, 255, 255), thickness=4)
                if fingers[2] == 1:
                    l, b = detector.findDistance(8, 12, imgCoppy)
                    if l < 50:
                        click = 1
                    if click:
                        click += 1
                        cv.rectangle(img3, (enterX - 5, enterY - 5), (enterX1 + 5, enterY1 + 5), (0, 255, 0), cv.FILLED)
                        cv.putText(img3, "Space", (frameR +4*size + 4*space+ int(size / 6), frameR + ((3) * (size + space)) + int(size) + int(size / 5)),cv.FONT_ITALIC, 1, (255, 255, 255), thickness=4)

                    if click >= 3 and l > 50:
                        #print('space')

                        keyboard.press(" ")
                        click = 0

            # capslock
            if capsX < xIndex <capsX1  and capsY < yIndex < capsY1:
                cv.rectangle(img3, (capsX - int(space/4), capsY - int(space/4)), (capsX1 + int(space/4), capsY1 + int(space/4)), (200, 255, 0), cv.FILLED)
                cv.putText(img3,"caps lock", (frameR +int(size/6),frameR +((3)*(size+space))+int(size)+int(size/5)),cv.FONT_ITALIC,1 , (255,255,255),thickness=4)
                if fingers[2] == 1:
                    l, b = detector.findDistance(8, 12, imgCoppy)
                    if l < 50:
                        click = 1
                    if click:
                        click += 1
                        cv.rectangle(img3, (capsX - int(space/4), capsY - int(space/4)), (capsX1 + int(space/4), capsY1 + int(space/4)), (0, 255, 0), cv.FILLED)
                        cv.putText(img3,"caps lock", (frameR +int(size/6),frameR +((3)*(size+space))+int(size)+int(size/5)),cv.FONT_ITALIC,1 , (255,255,255),thickness=4)
                    if click >= 3 and l > 50:
                        click = 0
                        if caps:
                            caps = False
                            # print("los")
                        else:
                            caps = True
                            # print("up")

            #exit
            if exitX < xIndex < exitX1 and exitY < yIndex < exitY1:
                cv.rectangle(img3, (exitX-int(space/4), exitY-int(space/4)), (exitX1+int(space/4), exitY1+int(space/4)), (0, 0, 200), cv.FILLED)
                cv.putText(img3, "Exit", (frameR +8*size + 4*space+ int(size/2)+int(space), frameR + ((3) * (size + space)) + int(size) + int(size / 5)),cv.FONT_ITALIC, 1, (255, 255, 255), thickness=4)
                if fingers[2] == 1:
                    l, b = detector.findDistance(8, 12, imgCoppy)
                    if l < 50:
                        click = 1
                    if click:
                        click += 1

                        cv.rectangle(img3, (exitX-int(space/4), exitY-int(space/4)), (exitX1+int(space/4), exitY1+int(space/4)), (0, 100, 255), cv.FILLED)
                        cv.putText(img3, "Exit", (frameR +8*size + 4*space+ int(size/2)+int(space), frameR + ((3) * (size + space)) + int(size) + int(size / 5)),cv.FONT_ITALIC, 1, (255, 255, 255), thickness=4)
                    if click >= 3 and l > 50:

                        close = True
                        click = 0


            # key
            for button in buttons:
                x,y = button.pos
                w,h = button.size
                key = button.text



                #key
                if x<xIndex<w and y<yIndex<h:
                    cv.rectangle(img3, (x-int(space/4), y-int(space/4)), (w+int(space/4), h+int(space/4)), (200, 255, 0), cv.FILLED)
                    cv.putText(img3, key, (x + int(space), y + int(3*space)), cv.FONT_ITALIC, 1, (255, 255, 255), thickness=3)
                    if fingers[2]==1:
                        l , b = detector.findDistance(8,12,imgCoppy)

                        if l<50 :
                            click =1
                        if click:
                            click +=1

                            cv.rectangle(img3, (x - int(space / 4)-int(space/3), y - int(space / 4)-int(space/3)),(w + int(space / 4) + int(space/3), h + int(space / 4)+ int(space/3)), (150, 200, 0), cv.FILLED)
                            cv.putText(img3, key, (x + int(space), y + int(3 * space)), cv.FONT_ITALIC, 1,(255, 255, 255), thickness=3)

                        if click>=3 and l>50:
                            keyboard.press(button.text)
                            click=0

    return img3



def main():

    buttonsUP = keyClass(keys)
    buttonsLOW = keyClass(keysLOW)
    global close
    close = False

    while True:
        sucess , img = cap.read()
        img = cv.flip(img,1)
        imgOUT = KeyBoard(img,buttonsUP , buttonsLOW)




        cv.imshow("result",imgOUT)
        

        if cv.waitKey(1) & 0xFF==ord('q') or close:
            if __name__=="__main__":
                break
            else:
                baseMain.main()
                break





if __name__ == '__main__':
    main()