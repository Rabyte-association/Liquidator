import signal
from xbox360controller import Xbox360Controller


class Axis1:
    value = 0

    def __init__(self, a):
        self.value = a


class Axis2:
    x = 0
    y = 0

    def __init__(self, a, b):
        self.x = a
        self.y = b


# gamepad object class
class Pad:
    button_A = False
    button_B = False
    button_X = False
    button_Y = False
    button_ThL = False
    button_ThR = False
    button_TR = False
    button_TL = False

    axisTL = Axis1(0)
    axisTR = Axis1(0)
    hatAxis = Axis2(0, 0)
    leftAxis = Axis2(0, 0)
    rightAxis = Axis2(0, 0)

    # updates controller object on every event
    def Update(self, element):
        name = element.name
        if name == "button_a":
            self.button_A = not self.button_A
        if name == "button_b":
            self.button_B = not self.button_B
        if name == "button_x":
            self.button_X = not self.button_X
        if name == "button_y":
            self.button_Y = not self.button_Y
        if name == "button_thumb_l":
            self.button_ThL = not self.button_ThL
        if name == "button_thumb_r":
            self.button_ThR = not self.button_ThR
        if name == "button_trigger_l":
            self.button_TL = not self.button_TL
        if name == "button_trigger_r":
            self.button_TR = not self.button_TR

        if name == "axis_l":
            self.leftAxis.x = round(element.x, 3)
            self.leftAxis.y = round(element.y, 3)
        if name == "axis_r":
            self.rightAxis.x = round(element.x, 3)
            self.rightAxis.y = round(element.y, 3)
        if name == "trigger_l":
            self.axisTL.value = round(element.value, 3)
        if name == "trigger_r":
            self.axisTR.value = round(element.value, 3)
        if name == "hat":
            self.hatAxis.x = round(element.x, 3)
            self.hatAxis.y = round(element.y, 3)

    # prints debug informations
    def ShowDebug(self):
        print('Pad Object: ')
        print('btnA: ' + str(self.button_A))
        print('btnB: ' + str(self.button_B))
        print('btnX: ' + str(self.button_X))
        print('btnY: ' + str(self.button_Y))
        print('btnThL: ' + str(self.button_ThL))
        print('btnThR: ' + str(self.button_ThR))
        print('btnTL: ' + str(self.button_TL))
        print('btnTR: ' + str(self.button_TR))

        print('leftAxis: x: ' + str(self.leftAxis.x) +
              ' y: ' + str(self.leftAxis.y))
        print('rigthAxis: x: ' + str(self.rightAxis.x) +
              ' y: ' + str(self.rightAxis.y))
        print('hat: x: ' + str(self.hatAxis.x) +
              ' y: ' + str(self.hatAxis.y))
        print('triggerL: val: ' + str(self.axisTL.value))
        print('triggerR: val: ' + str(self.axisTR.value))

    def on_button_pressed(self, button):  # event button press
        self.Update(button)

    def on_button_released(self, button):  # event button release
        self.Update(button)

    def on_axis_moved(self, axis):  # event axis move
        self.Update(axis)

    def Initialize(self):
        try:
            with Xbox360Controller(0, axis_threshold=0) as controller:
                # Buttons events init
                controller.button_a.when_pressed = self.on_button_pressed
                controller.button_a.when_released = self.on_button_released

                controller.button_b.when_pressed = self.on_button_pressed
                controller.button_b.when_released = self.on_button_released
                controller.button_y.when_pressed = self.on_button_pressed
                controller.button_y.when_released = self.on_button_released
                controller.button_x.when_pressed = self.on_button_pressed
                controller.button_x.when_released = self.on_button_released
                controller.button_thumb_l.when_pressed = self.on_button_pressed
                controller.button_thumb_l.when_released = self.on_button_released
                controller.button_thumb_r.when_pressed = self.on_button_pressed
                controller.button_thumb_r.when_released = self.on_button_released
                controller.button_trigger_l.when_pressed = self.on_button_pressed
                controller.button_trigger_l.when_released = self.on_button_released
                controller.button_trigger_r.when_pressed = self.on_button_pressed
                controller.button_trigger_r.when_released = self.on_button_released
                # axes move events init
                controller.axis_l.when_moved = self.on_axis_moved
                controller.axis_r.when_moved = self.on_axis_moved
                controller.trigger_l.when_moved = self.on_axis_moved
                controller.trigger_r.when_moved = self.on_axis_moved
                controller.hat.when_moved = self.on_axis_moved

                # rumble when initialization complete
                if controller.has_rumble:
                    controller.set_rumble(0, 1, 200)
                signal.pause()
        except KeyboardInterrupt:
            pass
