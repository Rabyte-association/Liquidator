import pickle
from time import sleep
from serial import Serial


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
    data = ''
datahold = DataHold()
datahold.data = ''
decoded = 0
xiaoID = '0'
picoID = '0'
def Initialize():
    serialxiao = Serial(port='/dev/ttyACM'+xiaoID, baudrate=115200, timeout=.1)
    serialpico = Serial(port='/dev/ttyACM'+picoID, baudrate=115200, timeout=.1)
    while True:
        if len(datahold.data)>2:
            decoded = pickle.loads(datahold.data)
            serialxiao.write(bytes(str('a' + str(decoded.hvbSpeed)), 'utf-8'))
            serialxiao.write(bytes(str('b' + str(decoded.hvbDir)), 'utf-8'))
            serialpico.write(bytes(str('x' + str(decoded.motorZ)), 'utf-8'))
            serialpico.write(bytes(str('y' + str(decoded.motoY)), 'utf-8'))
            serialpico.write(bytes(str('a' + str(decoded.motorX1)), 'utf-8'))
            serialpico.write(bytes(str('b' + str(decoded.motorX2)), 'utf-8'))
