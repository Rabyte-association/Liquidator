from inputs import get_gamepad
import math


class Axis2:
    x = 0
    y = 0

    def __init__(self, a, b):
        self.x = a
        self.y = b


class XboxController(object):
    MAX_TRIG_VAL =  math.pow(2, 8)
    MAX_JOY_VAL =  math.pow(2, 15)

    leftAxis = Axis2(0, 0)
    rightAxis = Axis2(0, 0)
    axisTL = 0
    axisTR = 0
    button_TL = 0
    button_TR = 0
    button_A = 0
    button_X = 0
    button_Y = 0
    button_B = 0
    ThL = 0
    ThR = 0
    Back = 0
    Start = 0
    hatAxis = Axis2(0, 0)

    def ShowDebug(self):
        print(self.button_A, self.button_B, self.Back, self.leftAxis.x, self.hatAxis.y)
    
    def Initialize(self):
            while True:
                events = get_gamepad()
                for event in events:
                    if event.code == 'ABS_Y':
                        # normalize between -1 and 1
                        self.leftAxis.y = round(event.state / XboxController.MAX_JOY_VAL, 4)
                    elif event.code == 'ABS_X':
                        # normalize between -1 and 1
                        self.leftAxis.x = round(event.state / XboxController.MAX_JOY_VAL, 4)
                    elif event.code == 'ABS_RY':
                        self.rightAxis.y =round(event.state/XboxController.MAX_JOY_VAL,4)  # normalize between -1 and 1
                    elif event.code == 'ABS_RX':
                        self.rightAxis.x = round(event.state /XboxController.MAX_JOY_VAL,4)  # normalize between -1 and 1
                    elif event.code == 'ABS_Z':
                        self.axisTL = round(event.state /XboxController.MAX_TRIG_VAL,4)  # normalize between 0 and 1
                    elif event.code == 'ABS_RZ':
                        self.axisTR = round(event.state / XboxController.MAX_TRIG_VAL,4)  # normalize between 0 and 1
                    elif event.code == 'BTN_TL':
                        self.button_TL = event.state
                    elif event.code == 'BTN_TR':
                        self.button_TR = event.state
                    elif event.code == 'BTN_SOUTH':
                        self.button_A = event.state
                    elif event.code == 'BTN_NORTH':
                        self.button_Y = event.state  # previously switched with X
                    elif event.code == 'BTN_WEST':
                        self.button_X = event.state  # previously switched with Y
                    elif event.code == 'BTN_EAST':
                        self.button_B = event.state
                    elif event.code == 'BTN_THUMBL':
                        self.ThL = event.state
                    elif event.code == 'BTN_THUMBR':
                        self.ThR = event.state
                    elif event.code == 'BTN_SELECT':
                        self.Back = event.state
                    elif event.code == 'BTN_START':
                        self.Start = event.state
                    elif event.code == 'BTN_TRIGGER_HAPPY1':
                        self.hatAxis.x = event.state
                    elif event.code == 'BTN_TRIGGER_HAPPY2':
                        self.hatAxis.x = event.state
                    elif event.code == 'BTN_TRIGGER_HAPPY3':
                        self.hatAxis.y = event.state
                    elif event.code == 'BTN_TRIGGER_HAPPY4':
                        self.hatAxis.y = event.state
