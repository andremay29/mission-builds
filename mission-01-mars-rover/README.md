# Mission 01: Mars Rover

A six-wheel rover inspired by NASA's Perseverance, built from a **VEX V5** robotics kit and programmed in **VEXcode**. Twelve logs, one real step of the build each.

**Cadets** build every program with Blocks (each log's README has the recipe). **Engineers** use the Python files, and from Log 10 on, C++ too.

| Log | Episode | Code | Status |
|---|---|---|---|
| 01 | Mission briefing | No code: the plan | Filmed when it airs |
| 02 | [Simulator test drive](log-02-simulator/) | `first_drive_vr.py` (VEXcode VR) | Ready |
| 03 | Unboxing the parts | No code | |
| 04 | Studying the real rover | No code: rocker-bogie explained | |
| 05 | The chassis | No code | |
| 06 | [Wheels, motors, power-up](log-06-power-up/) | `motor_check.py` | Ready, tune ports to the build |
| 07 | [First drive](log-07-first-drive/) | `arcade_drive.py` + Blocks recipe | Ready, tune ports to the build |
| 08 | Fixing what broke | Fixes get added to the log they belong to | |
| 09 | The camera mast | Mast motor added to Log 12's config | |
| 10 | [Same rover, real code](log-10-real-code/) | `arcade_drive.cpp` (C++) next to the Python | Ready |
| 11 | [Teaching it to drive itself](log-11-autonomous/) | `autonomous_route.py` | Ready, tune distances on your floor |
| 12 | [The Mars mission](log-12-mars-mission/) | `mars_mission.py` | Ready, tune the route to your terrain |

"Ready" means the program passes this repo's tests (see [tests/](../tests/)). Each one gets a final update after it runs on the real rover in its episode.

## The robot config

Every program starts with a **ROBOT CONFIG** section. Out of the box it assumes:

| Motor | Port | Reversed? |
|---|---|---|
| Left front | 1 | No |
| Left back | 2 | No |
| Right front | 9 | Yes |
| Right back | 10 | Yes |

"Reversed" is for motors mounted facing the other way, so "forward" means forward on both sides. If your build uses different ports or more motors, change the lists at the top of the program; nothing else needs to change.
