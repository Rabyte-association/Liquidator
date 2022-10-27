import pickle


class Motor:
    speed = 0
    direction = 0

    def __init__(self, a, b) -> None:
        self.speed = a
        self.direction = b


class Struct:
    voltage = 12
    motorL = Motor(4, 21)
    motorR = Motor(20, -37)
    ledRGB = [255, 128, 64]
    password = "abc123"

    def __bytes__(self):
        return

    def Print(self):
        print("voltage: " + str(self.voltage))
        print("motorL: s:" + str(self.motorL.speed) +
              " d:" + str(self.motorL.direction))
        print("motorR: s:" + str(self.motorR.speed) +
              " d:" + str(self.motorR.direction))
        print("ledRGB: " + str(self.ledRGB))
        print("password: " + self.password)


def Encode(struct):
    return pickle.dumps(struct)


def Decode(stream):
    return pickle.loads(stream)


struct = Struct()
struct.Print()

stream = Encode(struct)
print(stream)

new = Decode(stream)
print(new.motorL.speed)
