import serial
import time

class Hvb_controller:
    def __init__(self, port):
        self.ser = serial.Serial(port, 9600)
    
    def send_pwm(self, movement, turn):
        data = 'a' + str(movement)
        data = bytes(data, 'ascii')
        self.ser.write(data)

        data = 'b' + str(turn)
        data = bytes(data, 'ascii')
        self.ser.write(data)

if __name__ == "__main__":
    hvb = Hvb_controller("COM7")
    while True:
        hvb.send_pwm(70, 60)
        print("rx: ", hvb.ser.read_until())
        time.sleep(0.5)