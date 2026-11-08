# ---------------------------------------------------------------
#  Mission Builds HQ | Mission 01, Log 06: Wheels, motors, power-up
#  Runs in VEXcode V5 (Python): codev5.vex.com or the VEXcode app
#
#  What it does: spins each drive motor by itself for one second,
#  so you can check every motor is plugged into the right port
#  and turning the right way. Lift the rover off the table first!
# ---------------------------------------------------------------
from vex import *

# ---------- ROBOT CONFIG: change these to match YOUR build ----------
# Each motor: (name shown on screen, port, reversed?)
# "reversed" is True for motors mounted facing the other way, so
# "forward" means forward on both sides of the rover.
DRIVE_MOTORS = [
    ("Left front",  Ports.PORT1,  False),
    ("Left back",   Ports.PORT2,  False),
    ("Right front", Ports.PORT9,  True),
    ("Right back",  Ports.PORT10, True),
]
TEST_SPEED_PERCENT = 30   # gentle speed for a bench test
# ---------------------------------------------------------------------

brain = Brain()

brain.screen.clear_screen()
brain.screen.set_cursor(1, 1)
brain.screen.print("MOTOR CHECK  battery: " + str(brain.battery.capacity()) + "%")
brain.screen.next_row()

all_ok = True
for name, port, is_reversed in DRIVE_MOTORS:
    motor = Motor(port, GearSetting.RATIO_18_1, is_reversed)

    if not motor.installed():
        # Nothing answered on this port: unplugged, loose cable, or wrong port.
        brain.screen.print(name + ": NOT FOUND, check the cable")
        print("MOTORCHECK name=" + name + " ok=0")
        all_ok = False
    else:
        brain.screen.print(name + ": spinning forward...")
        motor.spin(FORWARD, TEST_SPEED_PERCENT, PERCENT)
        wait(1, SECONDS)
        motor.stop()
        print("MOTORCHECK name=" + name + " ok=1")
    brain.screen.next_row()
    wait(0.5, SECONDS)

if all_ok:
    brain.screen.print("ALL MOTORS GO")
else:
    brain.screen.print("FIX THE MOTORS ABOVE, THEN RUN AGAIN")
print("MOTORCHECK result=" + ("GO" if all_ok else "NO-GO"))
