# Pre-flight check

[`systems_check.py`](systems_check.py) runs on the rover's Brain (VEXcode V5, Python). Nothing moves, so it's safe on the table.

It checks:

- **Battery:** at least 50% (change `MIN_BATTERY_PERCENT`).
- **Every motor:** plugged in and answering, and not over 50 °C (change `MAX_MOTOR_TEMP_C`). Warm motors lose power, so let them cool between hard runs.

The Brain shows **RESULT: GO** or **NO-GO**, and the console gets `PREFLIGHT` lines that the [mission screen](../mission-screen/) reads. The line format is in [docs/telemetry-format.md](../../docs/telemetry-format.md).

**Cadet track:** in Blocks, use `print (Brain battery capacity in %) on Brain` and `print (LeftFront temperature in %) on Brain` from Sensing, one line per motor.
