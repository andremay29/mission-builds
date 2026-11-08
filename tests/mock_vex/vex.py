"""A small stand-in for VEXcode V5's Python `vex` module, for testing on a computer.

It covers only the parts of the API the Mission Builds programs use. Every call is
recorded on `SIM`, and the controller sticks and buttons are driven by functions of
simulated time, so a test can say "push the stick forward for 1 second, then press A"
and check what the motors and screen did.
"""

# ---------------------------------------------------------------- simulator state


class StopProgram(Exception):
    """Raised by wait() when a test's time budget runs out (ends endless loops)."""


class _Sim:
    def reset(self):
        self.time_ms = 0.0
        self.time_limit_ms = 10_000
        self.axes = {}           # "axis3" -> function(t_seconds) -> -100..100
        self.buttons = {}        # "buttonA" -> function(t_seconds) -> bool
        self.missing_ports = set()
        self.motor_temps = {}    # port index -> degrees C
        self.battery = 90
        self.brain_screen = []   # every string printed to the Brain screen
        self.controller_screen = []
        self.spins = []          # (t_ms, motor_name, direction, velocity)
        self.drive_log = []      # ("drive"|"turn", direction, amount, units)
        self.timer_start_ms = 0.0

    def now(self):
        return self.time_ms / 1000.0

    def advance(self, ms):
        self.time_ms += ms
        if self.time_ms > self.time_limit_ms:
            raise StopProgram()


SIM = _Sim()
SIM.reset()

# ---------------------------------------------------------------- constants

FORWARD, REVERSE = "forward", "reverse"
LEFT, RIGHT = "left", "right"
PERCENT, RPM = "percent", "rpm"
MSEC, SECONDS = "msec", "seconds"
MM, INCHES, DEGREES, TURNS = "mm", "inches", "degrees", "turns"
PRIMARY, PARTNER = "primary", "partner"
BRAKE, COAST, HOLD = "brake", "coast", "hold"


class TemperatureUnits:
    CELSIUS = "celsius"
    FAHRENHEIT = "fahrenheit"


CELSIUS = TemperatureUnits.CELSIUS


class GearSetting:
    RATIO_36_1 = "36:1"
    RATIO_18_1 = "18:1"
    RATIO_6_1 = "6:1"


class Ports:
    pass


for _i in range(1, 22):
    setattr(Ports, "PORT%d" % _i, _i - 1)   # VEX numbers ports from 0 internally


def wait(amount, units=MSEC):
    SIM.advance(amount * 1000 if units == SECONDS else amount)


# ---------------------------------------------------------------- brain


class _Screen:
    def __init__(self, sink):
        self._sink = sink

    def print(self, *parts):
        self._sink.append(" ".join(str(p) for p in parts))

    def clear_screen(self, *args):
        self._sink.append("<clear>")

    def set_cursor(self, row, col):
        pass

    def next_row(self):
        pass

    def new_line(self):
        pass


class _Battery:
    def capacity(self, *args):
        return SIM.battery


class _Timer:
    def clear(self):
        SIM.timer_start_ms = SIM.time_ms

    def time(self, units=MSEC):
        elapsed = SIM.time_ms - SIM.timer_start_ms
        return elapsed / 1000.0 if units == SECONDS else elapsed


class Brain:
    def __init__(self):
        self.screen = _Screen(SIM.brain_screen)
        self.battery = _Battery()
        self.timer = _Timer()


# ---------------------------------------------------------------- controller


class _Axis:
    def __init__(self, name):
        self._name = name

    def position(self, *args):
        fn = SIM.axes.get(self._name)
        return int(fn(SIM.now())) if fn else 0


class _Button:
    def __init__(self, name):
        self._name = name

    def pressing(self):
        fn = SIM.buttons.get(self._name)
        return bool(fn(SIM.now())) if fn else False


class Controller:
    def __init__(self, kind=PRIMARY):
        for n in range(1, 5):
            setattr(self, "axis%d" % n, _Axis("axis%d" % n))
        for b in ("A", "B", "X", "Y", "Up", "Down", "Left", "Right", "L1", "L2", "R1", "R2"):
            setattr(self, "button" + b, _Button("button" + b))
        self.screen = _Screen(SIM.controller_screen)


# ---------------------------------------------------------------- motors


class Motor:
    def __init__(self, port, gearing=GearSetting.RATIO_18_1, reversed=False):
        if not isinstance(port, int) or not 0 <= port <= 20:
            raise ValueError("bad port: %r" % (port,))
        self.port = port
        self.reversed = reversed

    @property
    def name(self):
        return "PORT%d" % (self.port + 1)

    def installed(self):
        return self.port not in SIM.missing_ports

    def spin(self, direction, velocity=50, units=PERCENT):
        if not -100 <= velocity <= 100:
            raise ValueError("velocity out of range: %r" % velocity)
        SIM.spins.append((SIM.time_ms, self.name, direction, velocity))

    def spin_for(self, direction, amount, units=DEGREES, *args, **kwargs):
        SIM.spins.append((SIM.time_ms, self.name, direction, ("for", amount, units)))
        SIM.advance(500)

    def stop(self, *args):
        SIM.spins.append((SIM.time_ms, self.name, "stop", 0))

    def temperature(self, units=CELSIUS):
        return SIM.motor_temps.get(self.port, 30.0)


class MotorGroup:
    def __init__(self, *motors):
        if not motors:
            raise ValueError("MotorGroup needs at least one motor")
        self.motors = motors

    def spin(self, direction, velocity=50, units=PERCENT):
        for m in self.motors:
            m.spin(direction, velocity, units)

    def stop(self, *args):
        for m in self.motors:
            m.stop()


class DriveTrain:
    def __init__(self, left, right, wheel_travel=319.19, track_width=295,
                 wheel_base=40, units=MM, gear_ratio=1.0):
        assert isinstance(left, MotorGroup) and isinstance(right, MotorGroup)
        self.left, self.right = left, right
        self.drive_velocity = self.turn_velocity = 50

    def set_drive_velocity(self, velocity, units=PERCENT):
        self.drive_velocity = velocity

    def set_turn_velocity(self, velocity, units=PERCENT):
        self.turn_velocity = velocity

    def drive_for(self, direction, distance, units=MM, *args, **kwargs):
        assert direction in (FORWARD, REVERSE) and distance >= 0
        SIM.drive_log.append(("drive", direction, distance, units))
        SIM.advance(1000)

    def turn_for(self, direction, angle, units=DEGREES, *args, **kwargs):
        assert direction in (LEFT, RIGHT) and angle >= 0
        SIM.drive_log.append(("turn", direction, angle, units))
        SIM.advance(1000)

    def stop(self, *args):
        SIM.drive_log.append(("stop",))
