# ---------------------------------------------------------------
#  Mission Builds HQ | Mission 02: Cyberdeck pre-flight check
#  Runs in VEXcode V5 (Python) on the rover's Brain
#
#  Checks the battery and every motor, shows GO / NO-GO on the Brain,
#  and prints PREFLIGHT lines to the console. Plug the Brain into the
#  cyberdeck by USB, open VEXcode's console, run this, then paste the
#  lines into the mission screen (or let it read them live, later).
#  Nothing moves: safe to run on the table.
# ---------------------------------------------------------------
from vex import *

# ---------- ROBOT CONFIG: change these to match YOUR build ----------
# Each motor: (short id, port number, reversed?)
MOTORS = [
    ("LF", 1, False),
    ("LB", 2, False),
    ("RF", 9, True),
    ("RB", 10, True),
]
MIN_BATTERY_PERCENT = 50   # below this, charge before a mission
MAX_MOTOR_TEMP_C = 50      # warm motors lose power; let them cool first
# ---------------------------------------------------------------------

brain = Brain()


def check_motor(motor_id, port_number, is_reversed):
    """Return (ok, temperature) for one motor and print its PREFLIGHT line."""
    motor = Motor(getattr(Ports, "PORT" + str(port_number)), GearSetting.RATIO_18_1, is_reversed)
    if not motor.installed():
        print("PREFLIGHT motor=" + motor_id + " port=" + str(port_number) + " ok=0 temp=na")
        return False, None
    temperature = round(motor.temperature(TemperatureUnits.CELSIUS))
    ok = temperature <= MAX_MOTOR_TEMP_C
    print("PREFLIGHT motor=" + motor_id + " port=" + str(port_number)
          + " ok=" + ("1" if ok else "0") + " temp=" + str(temperature))
    return ok, temperature


brain.screen.clear_screen()
brain.screen.set_cursor(1, 1)
brain.screen.print("PRE-FLIGHT CHECK")
brain.screen.next_row()

battery = brain.battery.capacity()
battery_ok = battery >= MIN_BATTERY_PERCENT
print("PREFLIGHT battery=" + str(battery))
brain.screen.print("Battery: " + str(battery) + "% " + ("OK" if battery_ok else "CHARGE ME"))
brain.screen.next_row()

all_ok = battery_ok
for motor_id, port_number, is_reversed in MOTORS:
    ok, temperature = check_motor(motor_id, port_number, is_reversed)
    if temperature is None:
        brain.screen.print(motor_id + " (port " + str(port_number) + "): NOT FOUND")
    else:
        brain.screen.print(motor_id + " (port " + str(port_number) + "): " + str(temperature)
                           + " C " + ("OK" if ok else "TOO HOT"))
    brain.screen.next_row()
    all_ok = all_ok and ok

result = "GO" if all_ok else "NO-GO"
print("PREFLIGHT result=" + result)
brain.screen.print("RESULT: " + result)
