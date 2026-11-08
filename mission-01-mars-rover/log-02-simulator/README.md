# Log 02: Simulator test drive

Practice driving a virtual robot in **VEXcode VR** before touching a real part. It's free and runs in your web browser: [vr.vex.com](https://vr.vex.com).

**The mission:** drive forward, turn right, drive forward again.

## Cadet track: Blocks

1. Open VEXcode VR and choose the **Grid Map** playground.
2. Under **when started**, drag in these blocks from **Drivetrain**:
   - `drive forward for 600 mm`
   - `turn right for 90 degrees`
   - `drive forward for 600 mm`
3. Press **Start** and watch it go.
4. **Challenge:** make it drive a full square. Tip: wrap two blocks in a `repeat 4` block from **Control**.

## Engineer track: Python

Switch the project to Python and paste in [`first_drive_vr.py`](first_drive_vr.py). The challenge at the bottom shows the square as a `for` loop.

## What to notice

Change one number, then test. If you change three things at once and it breaks, you won't know which one did it. That's rule one of robotics, in the simulator and on the real rover.
