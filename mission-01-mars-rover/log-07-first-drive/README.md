# Log 07: First drive

Driving the rover with the V5 controller, "arcade" style:

| Control | What it does |
|---|---|
| Left stick, up and down | Forward and backward |
| Right stick, left and right | Turn |
| Hold **R1** | Turtle mode: half speed for tight spots |

## How arcade drive works

Each side of the rover gets its own speed:

- **Left side = forward + turn**
- **Right side = forward − turn**

Push straight forward and both sides match, so you go straight. Push the turn stick right and the left side speeds up while the right side slows down, so the rover swings right, like a tank.

## Cadet track: Blocks

Set up **Devices** first: two motor groups, `LeftDrive` and `RightDrive` (right side reversed), plus `Controller1`. Then:

```
when started
forever
    set LeftDrive velocity to  (Controller1 Axis3 position) + (Controller1 Axis1 position)  %
    set RightDrive velocity to (Controller1 Axis3 position) - (Controller1 Axis1 position)  %
    spin LeftDrive forward
    spin RightDrive forward
    wait 0.02 seconds
```

**Shortcut:** if you add a **Drivetrain** and a **Controller** in Devices, VEXcode can drive the rover with no blocks at all. Building it yourself is how you learn what's happening underneath.

## Engineer track: Python

[`arcade_drive.py`](arcade_drive.py) adds three things the blocks version doesn't have:

- a **deadband**, so a stick resting slightly off-center doesn't make the rover creep;
- a **clamp**, so speeds never go past 100%;
- **turtle mode** on R1.

Want to see it in C++? That's [Log 10](../log-10-real-code/).
