from controller import controller
import threading
from time import sleep
from controller import Wirelesscontroller
from controller import windowsController

#Enkodowanie danych po stronie sterującego

class Struct:
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
    led = 0             #zmiana stanu ledow => Select
    
    def __bytes__(self):
        return

Data = Struct()

#pad= controller.Pad()
#pad = Wirelesscontroller.Pad() #[*] rip
pad = windowsController.Pad()

MAX_VEL = 300       #w jednostkach hoverboarda
NORM_VEL = 150
MIN_VEL = 40
MAX_DIR = 100

def Initialize():
    controllerThread = threading.Thread(target = pad.Initialize)
    controllerThread.start()
    while True:
        if pad.button_X == 0:                                   
            if pad.button_B == 0:                               #B  - przycisk "nitro"
                if abs(pad.leftAxis.y * NORM_VEL) < MIN_VEL:
                    Data.hvbSpeed = 0
                else:
                    Data.hvbSpeed = pad.leftAxis.y * NORM_VEL
            else:
                if abs(pad.leftAxis.y * MAX_VEL) < MIN_VEL:
                    Data.hvbSpeed = 0
                else:
                    Data.hvbSpeed = pad.leftAxis.y * MAX_VEL
            Data.hvbDir = pad.leftAxis.x * MAX_DIR
            Data.HVB_ARM = pad.buttonStart                      #przekaźnik 
            Data.led = pad.buttonSelect
            Data.endstopOvr = pad.button_Y
            Data.homing = pad.button_A
            Data.motorY = pad.rightAxis.x
            Data.motorZ = pad.rightAxis.y
            Data.motorX1 = pad.axisTR - pad.button_TR        
            Data.motorX2 = pad.axisTL - pad.button_TL           #jak się nacisnie oba na raz, nic się nie dzieje
        else:   
            Data.hvbDir = 0
            Data.hvbSpeed = 0
            Data.hvbDir = 0
            Data.HVB_ARM = 0
            Data.led = 0
            Data.motorY = 0
            Data.motorZ = 0
            Data.motorX1 = 0
            Data.motorX2 = 0


