import pickle
from time import sleep
from serial import Serial
import threading


class Struct:       #ten kod nic nie robi, ale jest jako podpowiedz
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

class DataHold:
    data = ""
datahold = DataHold()
datahold.data = ""
xiaoID = '0'
picoID = '1'
def Initialize():
    serialpico = Serial(port='/dev/ttyACM'+picoID, baudrate=115200, timeout=None)
    serialxiao = Serial(port='/dev/ttyACM'+xiaoID, baudrate=115200, timeout=0.1)
    while True:
        if len(datahold.data)>2:
            try:
                decoded = pickle.loads(datahold.data)
                serialpico.write(bytes('y' + str(decoded.motorY), 'utf-8'))
                serialpico.write(bytes('z' + str(decoded.motorZ), 'utf-8'))
                serialpico.write(bytes('a' + str(decoded.motorX2), 'utf-8'))
                serialpico.write(bytes('b' + str(decoded.motorX1), 'utf-8'))
                serialpico.write(bytes('h' + str(decoded.HVB_ARM), 'utf-8'))
                serialpico.write(bytes('l' + str(decoded.led), 'utf-8'))
                serialxiao.write(bytes('x' + str(decoded.hvbSpeed), 'utf-8'))
                serialxiao.write(bytes('b' + str(decoded.hvbDir), 'utf-8'))
            except:
                print("err")
                decoded = b'\x80\x04\x95\x9e\x00\x00\x00\x00\x00\x00\x00\x8c\x13Comms.encode_client\x94\x8c\x06Struct\x94\x93\x94)\x81\x94}\x94(\x8c\x08hvbSpeed\x94K\x00\x8c\x06hvbDir\x94K\x00\x8c\x07HVB_ARM\x94K\x00\x8c\x03led\x94K\x00\x8c\nendstopOvr\x94K\x00\x8c\x06homing\x94K\x00\x8c\x06motorY\x94K\x00\x8c\x06motorZ\x94K\x00\x8c\x07motorX1\x94K\x00\x8c\x07motorX2\x94K\x00ub.'

