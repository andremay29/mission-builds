# ---------------------------------------------------------------
#  Mission Builds HQ | Mission 01, Log 07: First drive
#  Runs in VEXcode V5 (Python): codev5.vex.com or the VEXcode app
#
#  Drive the rover with the V5 controller, "arcade" style:
#    Left stick up/down   (Axis 3) = forward and backward
#    Right stick left/right (Axis 1) = turn
#    Hold R1              = turtle mode (half speed, for tight spots)
# ---------------------------------------------------------------
from vex import *

# ---------- ROBOT CONFIG: change these to match YOUR build ----------
LEFT_PORTS = [Ports.PORT1, Ports.PORT2]
RIGHT_PORTS = [Ports.PORT9, Ports.PORT10]
DEADBAND = 5          # ignore tiny stick wiggles below this (out of 100)
TURTLE_SCALE = 0.5    # turtle mode speed: 0.5 = half speed
# ---------------------------------------------------------------------

brain = Brain()
controller_1 = Controller(PRIMARY)

# The right side is "reversed" because those motors face the other way.
left_drive = MotorGroup(*[Motor(p, GearSetting.RATIO_18_1, False) for p in LEFT_PORTS])
right_drive = MotorGroup(*[Motor(p, GearSetting.RATIO_18_1, True) for p in RIGHT_PORTS])


def deadband(value):
    """Treat tiny stick movements as zero, so the rover doesn't creep."""
    if abs(value) < DEADBAND:
        return 0
    return value


def clamp(value):
    """Keep a speed between -100 and 100 percent."""
    return max(-100, min(100, value))


def arcade_mix(forward, turn, scale=1.0):
    """Turn two stick values into left and right wheel speeds.

    Pushing forward spins both sides forward. Turning right speeds up
    the left side and slows the right side, like a tank.
    """
    left = clamp(forward + turn) * scale
    right = clamp(forward - turn) * scale
    return left, right


brain.screen.clear_screen()
brain.screen.set_cursor(1, 1)
brain.screen.print("MISSION BUILDS | ROVER ONLINE")
controller_1.screen.print("ROVER ONLINE")

while True:
    forward = deadband(controller_1.axis3.position())
    turn = deadband(controller_1.axis1.position())
    scale = TURTLE_SCALE if controller_1.buttonR1.pressing() else 1.0

    left_speed, right_speed = arcade_mix(forward, turn, scale)
    left_drive.spin(FORWARD, left_speed, PERCENT)
    right_drive.spin(FORWARD, right_speed, PERCENT)

    # Check the sticks 50 times a second. Faster than that wastes battery.
    wait(20, MSEC)
