# ---------------------------------------------------------------
#  Mission Builds HQ | Mission 01, Log 12: The Mars mission
#  Runs in VEXcode V5 (Python): codev5.vex.com or the VEXcode app
#
#  The final run: a countdown, then the rover drives to each "sample
#  site" on your Mars terrain, stops, scans with its camera mast,
#  and logs a telemetry line. Press A to launch, hold B to abort.
#
#  The TLM lines it prints are what the Mission 02 cyberdeck will
#  read later (see docs/telemetry-format.md).
# ---------------------------------------------------------------
from vex import *

# ---------- ROBOT CONFIG: change these to match YOUR build ----------
LEFT_PORTS = [Ports.PORT1, Ports.PORT2]
RIGHT_PORTS = [Ports.PORT9, Ports.PORT10]
MAST_PORT = None            # port of the mast motor, e.g. Ports.PORT5; None = no mast motor
WHEEL_TRAVEL_MM = 319.19
TRACK_WIDTH_MM = 295
WHEEL_BASE_MM = 40
DRIVE_SPEED_PERCENT = 35
TURN_SPEED_PERCENT = 20
# ---------------------------------------------------------------------

# ---------- THE MISSION: moves, plus sample sites to stop at ----------
MISSION = [
    ("drive", 500),
    ("site", "Jezero Delta"),
    ("turn", 45),
    ("drive", 400),
    ("site", "Crater Rim"),
    ("turn", -90),
    ("drive", 350),
    ("site", "Home Base"),
]
# ------------------------------------------------------------------------

brain = Brain()
controller_1 = Controller(PRIMARY)

left_drive = MotorGroup(*[Motor(p, GearSetting.RATIO_18_1, False) for p in LEFT_PORTS])
right_drive = MotorGroup(*[Motor(p, GearSetting.RATIO_18_1, True) for p in RIGHT_PORTS])
drivetrain = DriveTrain(left_drive, right_drive, WHEEL_TRAVEL_MM, TRACK_WIDTH_MM,
                        WHEEL_BASE_MM, MM, 1)
drivetrain.set_drive_velocity(DRIVE_SPEED_PERCENT, PERCENT)
drivetrain.set_turn_velocity(TURN_SPEED_PERCENT, PERCENT)
mast = Motor(MAST_PORT, GearSetting.RATIO_18_1, False) if MAST_PORT is not None else None


def show(line1, line2=""):
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print(line1)
    if line2:
        brain.screen.next_row()
        brain.screen.print(line2)
    controller_1.screen.clear_screen()
    controller_1.screen.set_cursor(1, 1)
    controller_1.screen.print(line1)


def telemetry(event, detail=""):
    """Print one telemetry line to the console (format: docs/telemetry-format.md)."""
    line = "TLM t=" + str(round(brain.timer.time(SECONDS), 1))
    line += " bat=" + str(brain.battery.capacity())
    line += " event=" + event
    if detail:
        line += " detail=" + detail.replace(" ", "_")
    print(line)


def scan_site(name):
    show("SITE: " + name, "Scanning...")
    telemetry("site", name)
    if mast is not None:
        mast.spin_for(FORWARD, 90, DEGREES)
        mast.spin_for(REVERSE, 90, DEGREES)
    else:
        wait(2, SECONDS)


def run_step(kind, value):
    if kind == "drive":
        drivetrain.drive_for(FORWARD if value >= 0 else REVERSE, abs(value), MM)
    elif kind == "turn":
        drivetrain.turn_for(RIGHT if value >= 0 else LEFT, abs(value), DEGREES)
    elif kind == "site":
        scan_site(value)
    else:
        raise ValueError("Unknown step: " + str(kind))


# ---- Pre-launch ----
show("MARS MISSION READY", "Press A to launch")
while not controller_1.buttonA.pressing():
    wait(20, MSEC)

for count in (3, 2, 1):
    show("T-minus " + str(count))
    wait(1, SECONDS)

brain.timer.clear()
show("LIFTOFF")
telemetry("launch")

# ---- The mission ----
aborted = False
for kind, value in MISSION:
    if controller_1.buttonB.pressing():
        aborted = True
        break
    run_step(kind, value)

drivetrain.stop()
elapsed = round(brain.timer.time(SECONDS), 1)
if aborted:
    telemetry("abort")
    show("MISSION ABORTED", "Time: " + str(elapsed) + " s")
else:
    telemetry("complete")
    show("MISSION COMPLETE", "Time: " + str(elapsed) + " s")
