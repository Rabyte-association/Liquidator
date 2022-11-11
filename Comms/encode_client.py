from controller import controller
import threading
from time import sleep
from controller import Wirelesscontroller

#Enkodowanie danych po stronie sterującego

class Struct:
    HVB_ARM = 0  #przekaźnik zasilania hvb, zmiana chwilowa
    stop = 0        #stop ruchu silnikow chwytaka
    hvbSpeed = 0
    hvbDir = 0
    motorY = 0
    motorZ = 0         #predkosc -x -> x
    motorX1 = 0         #chwytak
    motorX2 = 0
    homing = 0          #powrót do domu osi na robocie
    cameraAngle = 0
    endstopOvr  = 0 #endstop override
    ledRGB = [255, 128, 64]
    
    def __bytes__(self):
        return



Data = Struct()

MAX_VEL = 400
MAX_DIR = 200

#pad= controller.Pad()
pad = Wirelesscontroller.Pad()

def Initialize(ControllerType):
    controllerThread = threading.Thread(target = pad.Initialize)
    controllerThread.start()
    while True:
        Data.homing = pad.button_Y 
        Data.hvbDir = pad.leftAxis.x * MAX_DIR
        Data.hvbSpeed = pad.leftAxis.y * MAX_VEL
        Data.motorY = pad.rightAxis.y
        Data.motorZ = pad.rightAxis.x
        Data.HVB_ARM = pad.buttonSelect
        Data.stop = pad.button_X
        if pad.axisTR==1:
            Data.motorX1 = 1
            pass
        elif pad.button_TR == 1:
            Data.motorX1 = -1
        else:
            Data.motorX1 = 0

        if pad.axisTL ==1:
            Data.motorX2 = 1
            pass
        elif pad.button_TL ==1:
            Data.motorX2 = -1
        else:
           Data.motorX2 = 0

    
