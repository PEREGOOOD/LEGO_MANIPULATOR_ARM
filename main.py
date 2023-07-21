#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

M1 = Motor(port = Port.C,positive_direction=Direction.CLOCKWISE,gears=None)
M2 = Motor(port = Port.B,positive_direction=Direction.COUNTERCLOCKWISE,gears=None)
GRIPPER = Motor(port = Port.A,positive_direction=Direction.CLOCKWISE,gears=None)

TS = TouchSensor(port = Port.S1)
CS = ColorSensor(port = Port.S2)


# Write your program here.
ev3.speaker.beep()

def F_position():

    while CS.color() != Color.WHITE:
        M2.run(150)
    M2.run(0)

    while not TS.pressed():
        M1.run(200)
    M1.stop()
    M1.reset_angle(0)
    M1.run_target(200, -290, then=Stop.HOLD, wait=True)

    
def close_gripper():
    GRIPPER.run_time(100, 2000, then=Stop.HOLD, wait=True)
    GRIPPER.reset_angle(0)
    
def open_gripper():
    GRIPPER.run_target(-100, -100, then=Stop.HOLD, wait=True)

def left():
    M1.run_target(200, 0, then=Stop.HOLD, wait=True)
    M2.run_time(-100, 3600,then=Stop.HOLD, wait=True)
    close_gripper()
    while CS.color() != Color.WHITE:
        M2.run(150)
    M2.run(0)
    M1.run_target(200, -220, then=Stop.HOLD, wait=True)
    M2.run_time(-100, 3600,then=Stop.HOLD, wait=True)
    open_gripper()


def right():
    M1.run_target(200, -590, then=Stop.HOLD, wait=True)
    M2.run_time(-100, 3600,then=Stop.HOLD, wait=True)
    close_gripper()
    while CS.color() != Color.WHITE:
        M2.run(150)
    M2.run(0)
    M1.run_target(200, -320, then=Stop.HOLD, wait=True)
    M2.run_time(-100, 3600,then=Stop.HOLD, wait=True)
    open_gripper()


F_position()
close_gripper()
open_gripper()
left()
F_position()
close_gripper()
open_gripper()
right()
F_position()






