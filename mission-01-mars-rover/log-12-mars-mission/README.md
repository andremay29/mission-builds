# Log 12: The Mars mission

The finale: a countdown, then the rover drives across a homemade Mars terrain, stops at each sample site, scans with its camera mast, and reports back.

## What `mars_mission.py` does

1. Waits for **A** on the controller, then counts down **3, 2, 1** on the Brain and controller.
2. Works through the `MISSION` list: drives, turns, and stops at each `("site", "name")`.
3. At each site, it turns the mast motor to "scan" (or pauses, if you didn't give the mast a motor).
4. Prints a **telemetry line** at launch, at each site, and at the end, like `TLM t=4.2 bat=88 event=site detail=Jezero_Delta`.
5. Shows **MISSION COMPLETE** and the total time. Hold **B** to abort between steps.

The site names come from real places: Perseverance landed in **Jezero Crater** and explored the remains of an ancient river delta there.

## Make it your own

- Rename the sites, add more, or change the route in `MISSION`.
- If you built a mast motor in Log 09, set `MAST_PORT` (for example `Ports.PORT5`).

## Why the telemetry lines matter

Those `TLM` lines are how the rover will talk to the cyberdeck in [Mission 02](../../mission-02-cyberdeck/). The format is in [docs/telemetry-format.md](../../docs/telemetry-format.md).
