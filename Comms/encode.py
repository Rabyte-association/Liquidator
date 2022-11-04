import pickle

#Enkodowanie danych po stronie sterującego
class HVB_Motor:
    speed = 0
    direction = 0

    def __init__(self, a, b) -> None:
        self.speed = a
        self.direction = b


class Struct:
    HVB_ARM = 0  #przekaźnik zasilania hvb
    stop = 0        #stop ruchu silnikow chwytaka
    HVB = HVB_Motor(0,0)
    motorY = 0
    motorZ = 0          #predkosc -x -> x
    motorX1 = 0         #chwytak
    motorX2 = 0
    homing = 0          #powrót do domu osi na robocie
    cameraAngle = 0
    ledRGB = [255, 128, 64]
    
    def __bytes__(self):
        return


def EncPrint(data):
    print("motorY: " + str(data.motorY) +" motorZ: " + str(data.motorZ))
    print("HVB: speed:" + str(data.HVB.speed) + " d:" + str(data.HVB.direction))
    print("ledRGB: " + str(data.ledRGB))


def Encode():
    return pickle.dumps(Struct)


def Decode(stream):
    return pickle.loads(stream)
