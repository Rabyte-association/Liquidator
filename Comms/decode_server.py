import pickle
from time import sleep
from serial import Serial


class Struct:       #ten kod nic nie robi, ale jest jako podpowiedz
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

class Decoder:
    WSrecv = '0'
    decoded = 0
    ACMID = '0'
    def Initialize(self):
        serial = Serial(port='/dev/ttyACM'+self.ACMID, baudrate=115200, timeout=.1)
        while True:
            if len(self.WSrecv)>2:
                self.decoded = pickle.loads(self.WSrecv)
                print(self.decoded.homing)
                serial.write(bytes(str('a' + str(self.decoded.homing)), 'utf-8'))