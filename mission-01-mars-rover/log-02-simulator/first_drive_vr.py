# ---------------------------------------------------------------
#  Mission Builds HQ | Mission 01, Log 02: Simulator test drive
#  Runs in VEXcode VR (free, in your web browser): vr.vex.com
#
#  CADET TRACK: build the same thing with blocks first (see the
#  README in this folder), then peek at this file to see what your
#  blocks look like as real Python code.
# ---------------------------------------------------------------

# VEXcode VR adds these lines for you in a new Python project.
from vexcode_vr import *

brain = Brain()
drivetrain = Drivetrain("drivetrain", 0)

# How far to drive on each leg, in millimeters (1000 mm = 1 meter).
LEG_LENGTH_MM = 600


def main():
    brain.print("Mission 01, Log 02: test drive")
    brain.new_line()

    # The three moves from the episode: forward, turn right, forward.
    drivetrain.drive_for(FORWARD, LEG_LENGTH_MM, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, LEG_LENGTH_MM, MM)

    brain.print("Test drive complete")
    brain.new_line()

    # CHALLENGE: can you make the robot drive a full square?
    # Hint: a square is 4 x (drive forward, turn right 90 degrees).
    # Try a "for" loop:
    #
    #     for side in range(4):
    #         drivetrain.drive_for(FORWARD, LEG_LENGTH_MM, MM)
    #         drivetrain.turn_for(RIGHT, 90, DEGREES)


# VEXcode VR starts your program with this line. Don't delete it.
vr_thread(main)
