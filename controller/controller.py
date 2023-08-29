import signal
#from xbox360controller import Xbox360Controller

#Controller translator magic class by LosPedros
class Axis2:
    x = 0
    y = 0

    def __init__(self, a, b):
        self.x = a
        self.y = b

class Pad:
    button_A = False
    button_B = False
    button_X = False
    button_Y = False
    thumb_left_pressed = 0
    thumb_right_pressed = 0
    button_TriggerRight = 0
    button_TriggerLeft = 0
    buttonStart = 0
    buttonSelect = 0

    axisTriggerLeft = 0
    axisTriggerRight = 0
    hatAxis = Axis2(0, 0)
    leftAxis = Axis2(0, 0)
    rightAxis = Axis2(0, 0)

    def buttonAPressed(self, button):
        self.button_A = True
    def buttonBPressed(self, button):
        self.button_B = True
    def buttonXPressed(self, button):
        self.button_X = True
    def buttonYPressed(self, button):
        self.button_Y = True
    def startPressed(self, button):
        self.buttonStart = True
    def selectPressed(self, button):
        self.buttonSelect = True
    def leftThumbPressed(self, button):
        self.thumb_left_pressed = True
    def rightThumbPressed(self, button):
        self.thumb_right_pressed = True
    def leftTriggerPressed(self, button):
        self.button_TriggerRight = True
    def rightTriggerPressed(self, button):
        self.button_TriggerRight = True
    def buttonAReleased(self, button):
        self.button_A = False
    def buttonBReleased(self, button):
        self.button_B = False
    def buttonXReleased(self, button):
        self.button_X = False
    def buttonYReleased(self, button):
        self.button_Y = False
    def startReleased(self, button):
        self.buttonStart = False
    def selectReleased(self, button):
        self.buttonSelect = False
    def leftThumbReleased(self, button):
        self.thumb_left_Released = False
    def rightThumbReleased(self, button):
        self.thumb_right_Released = False
    def leftTriggerReleased(self, button):
        self.button_TriggerRight = False
    def rightTriggerReleased(self, button):
        self.button_TriggerRight = False
    def updateLeftJoystick(self, button):
        self.leftAxis = Axis2(round(button.x, 3), round(button.y, 3))
    def updateRightJoystick(self, button):
        self.rightAxis = Axis2(round(button.x, 3), round(button.y, 3))
    def updateHat(self, button):
        self.rightAxis = Axis2(round(button.x, 3), round(button.y, 3))
    def triggerRightUpdate(self, button):
        self.axisTriggerRight = round(button.value, 3)
    def triggerLeftUpdate(self, button):
        self.axisTriggerLeft = round(button.value, 3)
    def Initialize(self):
        controller = Xbox360Controller(0, axis_threshold=0)
        controller.button_a.when_pressed = self.buttonAPressed
        controller.button_a.when_released = self.buttonAReleased
        controller.button_start.when_pressed = self.startPressed
        controller.button_start.when_released = self.startReleased
        controller.button_b.when_pressed = self.buttonBPressed
        controller.button_b.when_released = self.buttonBReleased
        controller.button_y.when_pressed = self.buttonYPressed
        controller.button_y.when_released = self.buttonYReleased
        controller.button_x.when_pressed = self.buttonXPressed
        controller.button_x.when_released = self.buttonXReleased
        controller.button_thumb_l.when_pressed = self.leftThumbPressed
        controller.button_thumb_l.when_released = self.leftThumbReleased
        controller.button_thumb_r.when_pressed = self.rightThumbPressed
        controller.button_thumb_r.when_released = self.rightThumbReleased
        controller.button_trigger_l.when_pressed = self.leftTriggerPressed
        controller.button_trigger_l.when_released = self.leftTriggerReleased
        controller.button_trigger_r.when_pressed = self.rightTriggerPressed
        controller.button_trigger_r.when_released = self.rightTriggerReleased
        # axes move events init
        controller.axis_l.when_moved = self.updateLeftJoystick
        controller.axis_r.when_moved = self.updateRightJoystick
        controller.trigger_l.when_moved = self.triggerLeftUpdate
        controller.trigger_r.when_moved = self.triggerRightUpdate
        controller.hat.when_moved = self.updateHat
