from controller import controller
import threading
from time import sleep
from controller import Wirelesscontroller
from controller import windowsController

#Enkodowanie danych po stronie sterującego

class HoverboardData:
    HVB_ARM = 0  #przekaźnik zasilania hvb, zmiana chwilowa => start
    stop = 0        #stop ruchu silnikow chwytaka => X
    hvbSpeed = 0
    hvbDir = 0
    motorY = 0          #winda na prawym sticku
    motorZ = 0         
    motorX1 = 0        #chwytak na triggerach i bumpraach
    motorX2 = 0        
    homing = 0          #powrót do domu osi na robocie => A
    cameraAngle = 0
    endstopOvr  = 0     #endstop override =>Y
    led = 0
    encode = False             #zmiana stanu ledow => Select
    
    def __bytes__(self):
        return

Data = HoverboardData()

#pad= controller.Pad()
#pad = Wirelesscontroller.Pad() #[*] rip
pad = windowsController.Pad()

MAX_VEL = 350       #w jednostkach hoverboarda
NORM_VEL = 200
MIN_VEL = 40
NORM_DIR = 100
MAX_DIR = 200
MIN_DIR = 20
rightDeadZone = 0.2

def Initialize():
    controllerThread = threading.Thread(target = pad.Initialize)
    controllerThread.start()
    while True:
        if pad.button_X != 0: 
            Data.hvbDir = 0
            Data.hvbSpeed = 0
            Data.hvbDir = 0
            Data.HVB_ARM = 0
            Data.led = 0
            Data.motorY = 0
            Data.motorZ = 0
            Data.motorX1 = 0
            Data.motorX2 = 0
            Data.encode = False
            break;                                  
        if pad.button_B == 0:                               #B  - przycisk "nitro"
            if abs(pad.leftAxis.y * NORM_VEL) < MIN_VEL:
                Data.hvbSpeed = 0
            else:
                Data.hvbSpeed = pad.leftAxis.y *- NORM_VEL
            if abs(pad.leftAxis.x * NORM_DIR) < MIN_DIR:
                Data.hvbDir = 0
            else:
                Data.hvbDir = pad.leftAxis.x *NORM_DIR
        else:
            if abs(pad.leftAxis.y * MAX_VEL) < MIN_VEL:
                Data.hvbSpeed = 0
            else:
                Data.hvbSpeed = pad.leftAxis.y * -MAX_VEL
            if abs(pad.leftAxis.x * MAX_DIR) < MIN_DIR:
                Data.hvbDir = 0
            else:
                Data.hvbDir = pad.leftAxis.x *MAX_DIR

        if pad.button_ThR == 1:
            Data.encode = True
        else:
            Data.encode = False

        #print(Data.hvbSpeed)
        Data.HVB_ARM = pad.buttonStart                      #przekaźnik 
        Data.led = pad.buttonSelect
        Data.endstopOvr = pad.button_Y
        Data.homing = pad.button_A
        if abs(pad.rightAxis.x) > rightDeadZone:
            Data.motorY = pad.rightAxis.x
        else:
            Data.motorY = 0
        if abs(pad.rightAxis.y)>rightDeadZone:
                Data.motorZ = pad.rightAxis.y
        else:
            Data.motorZ = 0
        Data.motorX1 = pad.axisTR - pad.button_TR        
        Data.motorX2 = pad.axisTL - pad.button_TL           #jak się nacisnie oba na raz, nic się nie dzieje

