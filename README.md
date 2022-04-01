# VirtualMouseAndKeyboard_opencv
in this prj we have a mouse and keyboard that we can use them just by our finger , it can be used for SMART TV and CAR display

# Libraries

you have to install `mediapipe` , `pip` , `opencv-python` , `pynput` , `tensorflow` , `autopy` , `numpy`

my python version was 3.8
and i wrote this program with `MacBook M1`


# Test Video
for `choosing` key tou have to put your `index finger` in the related area and for `clicking` you have to put your `middle finger next to your index` and for exit in the `virtual Mouse` you have to show your first three fingers.

![](https://github.com/mohammadst99/VirtualMouseAndKeyboard_opencv/blob/main/testGIF.gif)

# Explain Code

i have already writen the `Virtual Mouse` and `Hand Detection` before and you can read about them in the links blow:
</br>

|Index|Topic|Image|Video|Description|
|:----:|:----:|:----:|:----:|:----:|
|1|VirtualMouse| <img src="https://github.com/mohammadst99/VirtualMouse_openCV/blob/main/test.gif" width="300" height="150" />  |[Watch Now](https://github.com/mohammadst99/VirtualMouse_openCV)     | we have a virtual mouse that you can adjust with your fingers.  </br> |
|2|GameHand| <img src="https://github.com/mohammadst99/game-HandDetection-/blob/main/test.gif" width="300" height="150" />  |[Watch Now](https://github.com/mohammadst99/game-HandDetection-)     | in this code i used `mediapipe` to detect the hand and gesture and also wrote a module to use it in further program </br> |

and about the KEYBOARD :
1. you have to import your camera to the python with using `opencv`
2. you have to specify the size of your camera `in the code i set it defult on ( 640,480 )`
3. you have to use opencv libraries to draw youe keyboard on your VideoCamera 
4. you have to specify the areaX and aresY for each key 
5. with using mediapip  and the HandTrackingModule you cam get your fingers position as (x,y)
6. and also i used my HandTrackingModule to know wich finger is up 
7. then you have to use `if` method to choose the key when the index Finger is in the related Area and click if your middle finger is nexto to your index 
8. and i use the `pynput` to press the key which you want to click 
