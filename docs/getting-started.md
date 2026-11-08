# Getting started

Everything here is free except the robot kit. You can do all of Log 02 with no robot at all.

## 1. Try the simulator (no robot needed)

1. Open [VEXcode VR](https://vr.vex.com) in Chrome, Edge, or Safari.
2. Pick a playground (the "Grid Map" is a good first one).
3. **Cadet track:** drag blocks from the left into the workspace under **when started**, then press **Start**.
4. **Engineer track:** switch the project to Python and paste in [first_drive_vr.py](../mission-01-mars-rover/log-02-simulator/first_drive_vr.py).

## 2. Code a real VEX V5 robot

You need a VEX V5 kit (Brain, battery, motors, controller) and **VEXcode V5**:

- In a browser: [codev5.vex.com](https://codev5.vex.com) in Chrome on a Chromebook, Mac, or Windows computer.
- As an app: download VEXcode V5 from [vexrobotics.com/vexcode](https://www.vexrobotics.com/vexcode).

Then:

1. **Make a project.** Blocks: a new Blocks project. Python or C++: **File → New Text Project**, then pick the language.
2. **Paste the program** from the log you're on, replacing what's there.
3. **Fix the ROBOT CONFIG section** at the top so the ports match where your motors are plugged in. The port number is printed next to each port on the Brain.
4. **Connect the Brain** with the USB cable (or wirelessly through the controller), then **Download** and **Run**.

The first time you run anything that moves, hold the rover or lift it off the table.

## 3. Blocks, Python, or C++?

Start wherever you're comfortable. [blocks-python-cpp.md](blocks-python-cpp.md) shows one program in all three so you can see how they line up.

## If something goes wrong

| What you see | Try this |
|---|---|
| A motor doesn't move | Run [motor_check.py](../mission-01-mars-rover/log-06-power-up/motor_check.py). It tells you which port isn't answering. |
| One side drives backward | Flip that side's `reversed` setting (True ↔ False) in ROBOT CONFIG. |
| The rover turns when you push straight | One motor is in the wrong port, or one side's `reversed` is wrong. |
| VEXcode won't connect | Use a different USB cable or port, turn the Brain off and on, and make sure the battery is charged. |
| Python error with a line number | Look at that line for a missing `:`, a typo, or wrong spacing at the start of the line. |

Still stuck? [Open an issue](https://github.com/andremay29/mission-builds/issues) and say which log, what you expected, and what happened.
