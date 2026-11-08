# Log 06: Wheels, motors, power-up

Before the first drive, check that every motor is alive, in the right port, and turning the right way.

**Lift the rover off the table first** (rest the chassis on a box so the wheels spin freely).

## What `motor_check.py` does

1. Shows the battery level on the Brain screen.
2. Spins each drive motor forward by itself for one second, slowly.
3. Says **NOT FOUND** for any motor that doesn't answer (unplugged, loose cable, or wrong port).
4. Ends with **ALL MOTORS GO** or a list of what to fix.

Watch each wheel as its name comes up. If a wheel spins **backward**, flip that motor's `True`/`False` in the ROBOT CONFIG section.

## Cadet track: Blocks

For each motor (configure them in **Devices** first): `spin LeftFront forward` → `wait 1 seconds` → `stop LeftFront`. Then repeat for the next motor.

## Engineer track: Python

Paste in [`motor_check.py`](motor_check.py) and set the ports. It also prints `MOTORCHECK` lines to the console, which comes in handy in Mission 02.
