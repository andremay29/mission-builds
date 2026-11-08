# Log 11: Teaching it to drive itself

The rover follows a list of moves with no one touching the controller. Press **A** to launch; press **B** to abort between moves.

## How it works

The route is a list, and the program works down it one step at a time:

```python
ROUTE = [
    ("drive", 600),   # forward 600 mm
    ("turn", 90),     # right 90 degrees
    ("drive", 400),
    ("pause", 1),     # wait 1 second
    ("turn", -90),    # negative = left
    ("drive", 300),
]
```

That's how real Mars rovers drive. Radio signals take minutes to reach Mars, so nobody can steer live with a joystick. Engineers send a list of commands, and the rover carries them out on its own.

## Cadet track: Blocks

Add a **Drivetrain** in Devices, then stack: `drive forward for 600 mm`, `turn right for 90 degrees`, `drive forward for 400 mm`, `wait 1 seconds`, `turn left for 90 degrees`, `drive forward for 300 mm`. Put `wait until Controller1 ButtonA pressed?` at the top so it waits for launch.

## Engineer track: Python

Paste in [`autonomous_route.py`](autonomous_route.py). To change the route, edit only the `ROUTE` list.

## Tuning on a real floor

- **It drives too far or too short?** Measure your wheel. `WHEEL_TRAVEL_MM` is how far one full wheel turn moves the rover (about 319 mm for a 4-inch wheel).
- **Turns come up short or long?** Adjust `TRACK_WIDTH_MM` (the distance between the left and right wheels) a little at a time.
- **Carpet vs. hard floor** changes everything. Tune on the surface you'll film on.
