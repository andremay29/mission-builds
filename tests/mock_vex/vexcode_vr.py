"""A small stand-in for VEXcode VR's Python module, for testing on a computer."""
from vex import SIM, FORWARD, REVERSE, LEFT, RIGHT, MM, INCHES, DEGREES  # noqa: F401


class Brain:
    def print(self, *parts):
        SIM.brain_screen.append(" ".join(str(p) for p in parts))

    def new_line(self):
        pass

    def clear(self):
        SIM.brain_screen.append("<clear>")


class Drivetrain:
    def __init__(self, name, index):
        self.name = name

    def drive_for(self, direction, distance, units=MM, *args, **kwargs):
        assert direction in (FORWARD, REVERSE) and distance >= 0
        SIM.drive_log.append(("drive", direction, distance, units))

    def turn_for(self, direction, angle, units=DEGREES, *args, **kwargs):
        assert direction in (LEFT, RIGHT) and angle >= 0
        SIM.drive_log.append(("turn", direction, angle, units))


def vr_thread(fn):
    fn()
