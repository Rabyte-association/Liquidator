"""import pygame
pygame.init()
joysticks = []
clock = pygame.time.Clock()
keepPlaying = True

# for al the connected joysticks
for i in range(0, pygame.joystick.get_count()):
    # create an Joystick object in our list
    joysticks.append(pygame.joystick.Joystick(i))
    # initialize them all (-1 means loop forever)
    joysticks[-1].init()
    # print a statement telling what the name of the controller is
    print ("Detected joystick "),joysticks[-1].get_name(),"'"
while keepPlaying:
    clock.tick(60)
    for event in pygame.event.get():
        # The 0 button is the 'a' button, 1 is the 'b' button, 2 is the 'x' button, 3 is the 'y' button
        print(event)
"""
import signal
from xbox360controller import Xbox360Controller


def on_button_pressed(button):
    print('Button {0} was pressed'.format(button.name))
    #print(controller.info())


def on_button_released(button):
    print('Button {0} was released'.format(button.name))


def on_axis_moved(axis):
    print(f'Axis {axis.name} moved to {axis.x} {axis.y}')
    print(axis.x)
   # print(controller.info)
def on_trigger_moved(trigger):
    print(trigger.value)

try:
    with Xbox360Controller(0, axis_threshold=0) as controller:
        # Button A events
        controller.button_a.when_pressed = on_button_pressed
        controller.button_a.when_released = on_button_released
       # print(controller)
        controller.button_b.when_pressed = on_button_pressed
        controller.button_b.when_released = on_button_released
        controller.button_y.when_pressed = on_button_pressed
        controller.button_y.when_released = on_button_released
        controller.button_x.when_pressed = on_button_pressed 
        controller.button_x.when_released = on_button_released
        # Left and right axis move event
        controller.axis_l.when_moved = on_axis_moved
        controller.trigger_l.when_moved = on_trigger_moved
        controller.axis_r.when_moved = on_axis_moved
        signal.pause()

except KeyboardInterrupt:
    
    pass