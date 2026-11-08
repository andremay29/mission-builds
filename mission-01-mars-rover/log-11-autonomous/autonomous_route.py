# ---------------------------------------------------------------
#  Mission Builds HQ | Mission 01, Log 11: Teaching it to drive itself
#  Runs in VEXcode V5 (Python): codev5.vex.com or the VEXcode app
#
#  The rover follows a list of moves on its own (no hands!).
#  Press A on the controller to launch. Press B to abort between moves.
#
#  CADET TRACK: change the numbers in ROUTE and watch what happens.
#  ENGINEER TRACK: the route is data, not code. That's the same idea
#  real rovers use: engineers on Earth send a list of commands, and
#  the rover works through them by itself.
# ---------------------------------------------------------------
from vex import *

# ---------- ROBOT CONFIG: change these to match YOUR build ----------
LEFT_PORTS = [Ports.PORT1, Ports.PORT2]
RIGHT_PORTS = [Ports.PORT9, Ports.PORT10]
WHEEL_TRAVEL_MM = 319.19   # distance one wheel turn covers (4-inch wheel)
TRACK_WIDTH_MM = 295       # distance between left and right wheels: measure yours!
WHEEL_BASE_MM = 40
DRIVE_SPEED_PERCENT = 40
TURN_SPEED_PERCENT = 25
# ---------------------------------------------------------------------

# ---------- THE ROUTE: each step is (move, amount) ----------
#   ("drive", 600)  = drive forward 600 mm   (negative = backward)
#   ("turn", 90)    = turn right 90 degrees  (negative = left)
#   ("pause", 2)    = wait 2 seconds
ROUTE = [
    ("drive", 600),
    ("turn", 90),
    ("drive", 400),
    ("pause", 1),
    ("turn", -90),
    ("drive", 300),
]
# --------------------------------------------------------------

brain = Brain()
controller_1 = Controller(PRIMARY)

left_drive = MotorGroup(*[Motor(p, GearSetting.RATIO_18_1, False) for p in LEFT_PORTS])
right_drive = MotorGroup(*[Motor(p, GearSetting.RATIO_18_1, True) for p in RIGHT_PORTS])
drivetrain = DriveTrain(left_drive, right_drive, WHEEL_TRAVEL_MM, TRACK_WIDTH_MM,
                        WHEEL_BASE_MM, MM, 1)
drivetrain.set_drive_velocity(DRIVE_SPEED_PERCENT, PERCENT)
drivetrain.set_turn_velocity(TURN_SPEED_PERCENT, PERCENT)


def show(message):
    """Print a message on the Brain screen and the controller."""
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print(message)
    controller_1.screen.clear_screen()
    controller_1.screen.set_cursor(1, 1)
    controller_1.screen.print(message)


def run_step(move, amount):
    """Carry out one step of the route."""
    if move == "drive":
        direction = FORWARD if amount >= 0 else REVERSE
        drivetrain.drive_for(direction, abs(amount), MM)
    elif move == "turn":
        direction = RIGHT if amount >= 0 else LEFT
        drivetrain.turn_for(direction, abs(amount), DEGREES)
    elif move == "pause":
        wait(amount, SECONDS)
    else:
        raise ValueError("Unknown move: " + str(move))


def wait_for_launch():
    show("READY. Press A to launch")
    while not controller_1.buttonA.pressing():
        wait(20, MSEC)


wait_for_launch()
aborted = False
number = 0
for move, amount in ROUTE:
    number += 1
    if controller_1.buttonB.pressing():
        aborted = True
        break
    show("Step " + str(number) + "/" + str(len(ROUTE)) + ": " + move + " " + str(amount))
    run_step(move, amount)

drivetrain.stop()
show("ABORTED" if aborted else "ROUTE COMPLETE")
