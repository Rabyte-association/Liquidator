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
    


    ledRGB = [255, 128, 64]

    def __bytes__(self):
        return

    def Print(self):
        print("motorY: " + str(self.motorY) +" motorZ: " + str(self.motorZ))
        print("HVB: speed:" + str(self.HVB.speed) + " d:" + str(self.HVB.direction))
        print("ledRGB: " + str(self.ledRGB))


def Encode(struct):
    return pickle.dumps(struct)


def Decode(stream):
    return pickle.loads(stream)


struct = Struct()
struct.Print()

stream = Encode(struct)
print(stream)

new = Decode(stream)
print(new.motorY)
