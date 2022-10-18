import time
from serial import Serial


class EmergencyButton():

    state = False
    port = '/dev/ttyUSB0'
    baudrate = 9600

    def Initialize(self):
        emergency_serial = Serial(
            port=self.port, baudrate=self.baudrate, timeout=.1)
        control_ping_interval = 1000
        control_ping = 0
        while True:
            control_ping += 1
            if control_ping == control_ping_interval:
                emergency_serial.write(bytes(str(33), 'utf-8'))
                print('control ping sended')
                control_ping = 0

            serial_input = emergency_serial.readline()
            serial_input = serial_input.decode('utf-8', 'ignore')
            serial_input = serial_input.strip('\r\n')

            if serial_input == '0':  # if button disabled
                self.state = False
            else:  # if button enabled
                self.state = True

            time.sleep(0)
