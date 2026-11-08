"""Tests for the Mission Builds robot programs.

They run each program against a fake VEX library (tests/mock_vex) that records
what the motors, drivetrain, and screens were told to do. Run from the repo root:

    python -m unittest discover -s tests -v
"""
import contextlib
import io
import os
import runpy
import shutil
import subprocess
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "mock_vex"))

import vex  # noqa: E402  (the mock)
from vex import SIM, StopProgram  # noqa: E402

M1 = os.path.join(ROOT, "mission-01-mars-rover")
M2 = os.path.join(ROOT, "mission-02-cyberdeck")


def run(path, time_limit_s=10):
    """Run a program until it finishes or its time budget ends. Returns console lines."""
    SIM.time_limit_ms = time_limit_s * 1000
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        try:
            runpy.run_path(path, run_name="__main__")
        except StopProgram:
            pass
    return out.getvalue().splitlines()


def last_speeds():
    """The most recent speed sent to each motor, by port name."""
    speeds = {}
    for _, name, direction, velocity in SIM.spins:
        speeds[name] = velocity if direction == vex.FORWARD else -velocity
    return speeds


class Base(unittest.TestCase):
    def setUp(self):
        SIM.reset()


class TestLog02Simulator(Base):
    def test_drives_forward_turns_right_drives_again(self):
        run(os.path.join(M1, "log-02-simulator", "first_drive_vr.py"))
        self.assertEqual(SIM.drive_log, [
            ("drive", "forward", 600, "mm"),
            ("turn", "right", 90, "degrees"),
            ("drive", "forward", 600, "mm"),
        ])
        self.assertIn("Test drive complete", SIM.brain_screen)


class TestLog06MotorCheck(Base):
    PATH = os.path.join(M1, "log-06-power-up", "motor_check.py")

    def test_all_motors_present(self):
        lines = run(self.PATH)
        forward_spins = [s for s in SIM.spins if s[2] == "forward"]
        self.assertEqual(len(forward_spins), 4)
        self.assertTrue(all(s[3] == 30 for s in forward_spins))
        self.assertIn("ALL MOTORS GO", SIM.brain_screen)
        self.assertEqual(lines[-1], "MOTORCHECK result=GO")

    def test_unplugged_motor_is_reported(self):
        SIM.missing_ports = {vex.Ports.PORT9}
        lines = run(self.PATH)
        self.assertEqual(len([s for s in SIM.spins if s[2] == "forward"]), 3)
        self.assertIn("Right front: NOT FOUND, check the cable", SIM.brain_screen)
        self.assertEqual(lines[-1], "MOTORCHECK result=NO-GO")


class TestLog07ArcadeDrive(Base):
    PATH = os.path.join(M1, "log-07-first-drive", "arcade_drive.py")

    def drive_with(self, **inputs):
        for name, value in inputs.items():
            if name.startswith("axis"):
                SIM.axes[name] = lambda t, v=value: v
            else:
                SIM.buttons[name] = lambda t, v=value: v
        run(self.PATH, time_limit_s=1)
        return last_speeds()

    def test_full_forward(self):
        speeds = self.drive_with(axis3=100)
        self.assertEqual(set(speeds.values()), {100})
        self.assertEqual(len(speeds), 4)

    def test_turn_right_while_driving(self):
        speeds = self.drive_with(axis3=50, axis1=50)
        self.assertEqual(speeds["PORT1"], 100)   # left side faster
        self.assertEqual(speeds["PORT10"], 0)    # right side slower

    def test_speeds_never_exceed_100(self):
        speeds = self.drive_with(axis3=100, axis1=100)
        self.assertEqual(speeds["PORT1"], 100)
        self.assertEqual(speeds["PORT9"], 0)

    def test_deadband_ignores_tiny_wiggles(self):
        speeds = self.drive_with(axis3=3, axis1=-4)
        self.assertEqual(set(speeds.values()), {0})

    def test_turtle_mode_halves_speed(self):
        speeds = self.drive_with(axis3=100, buttonR1=True)
        self.assertEqual(set(speeds.values()), {50})

    def test_loop_runs_fifty_times_a_second(self):
        self.drive_with(axis3=100)
        updates = [s for s in SIM.spins if s[1] == "PORT1"]
        self.assertIn(len(updates), (50, 51))   # one second of 20 ms loops, counting t=0

    def test_screen_says_online(self):
        self.drive_with()
        self.assertIn("MISSION BUILDS | ROVER ONLINE", SIM.brain_screen)


class TestLog11Autonomous(Base):
    PATH = os.path.join(M1, "log-11-autonomous", "autonomous_route.py")

    def test_waits_for_launch(self):
        run(self.PATH, time_limit_s=3)
        self.assertEqual(SIM.drive_log, [])
        self.assertIn("READY. Press A to launch", SIM.brain_screen)

    def test_runs_whole_route(self):
        SIM.buttons["buttonA"] = lambda t: t >= 1
        run(self.PATH, time_limit_s=30)
        self.assertEqual(SIM.drive_log, [
            ("drive", "forward", 600, "mm"),
            ("turn", "right", 90, "degrees"),
            ("drive", "forward", 400, "mm"),
            ("turn", "left", 90, "degrees"),
            ("drive", "forward", 300, "mm"),
            ("stop",),
        ])
        self.assertEqual(SIM.brain_screen[-1], "ROUTE COMPLETE")

    def test_b_aborts_between_steps(self):
        SIM.buttons["buttonA"] = lambda t: t >= 1
        SIM.buttons["buttonB"] = lambda t: t >= 2.5
        run(self.PATH, time_limit_s=30)
        self.assertEqual(len([d for d in SIM.drive_log if d[0] != "stop"]), 2)
        self.assertEqual(SIM.brain_screen[-1], "ABORTED")


class TestLog12MarsMission(Base):
    PATH = os.path.join(M1, "log-12-mars-mission", "mars_mission.py")

    def test_full_mission_logs_telemetry(self):
        SIM.buttons["buttonA"] = lambda t: t >= 0.5
        lines = run(self.PATH, time_limit_s=60)
        events = [ln.split("event=")[1].split()[0] for ln in lines if ln.startswith("TLM ")]
        self.assertEqual(events, ["launch", "site", "site", "site", "complete"])
        self.assertIn("detail=Jezero_Delta", lines[1])
        self.assertIn("T-minus 1", SIM.brain_screen)
        self.assertEqual(SIM.brain_screen[-2], "MISSION COMPLETE")
        self.assertEqual(SIM.drive_log[-1], ("stop",))

    def test_telemetry_lines_are_key_value(self):
        SIM.buttons["buttonA"] = lambda t: True
        lines = run(self.PATH, time_limit_s=60)
        for line in (ln for ln in lines if ln.startswith("TLM ")):
            fields = dict(part.split("=", 1) for part in line.split()[1:])
            self.assertIn("t", fields)
            self.assertEqual(fields["bat"], "90")
            float(fields["t"])

    def test_abort(self):
        SIM.buttons["buttonA"] = lambda t: True
        SIM.buttons["buttonB"] = lambda t: t >= 4
        lines = run(self.PATH, time_limit_s=60)
        self.assertTrue(lines[-1].endswith("event=abort"))
        self.assertEqual(SIM.brain_screen[-2], "MISSION ABORTED")


class TestPreflight(Base):
    PATH = os.path.join(M2, "preflight", "systems_check.py")

    def test_go(self):
        lines = run(self.PATH)
        self.assertEqual(lines[0], "PREFLIGHT battery=90")
        self.assertEqual(lines[1], "PREFLIGHT motor=LF port=1 ok=1 temp=30")
        self.assertEqual(lines[-1], "PREFLIGHT result=GO")
        self.assertEqual(SIM.spins, [])   # nothing moves during pre-flight

    def test_hot_motor_is_no_go(self):
        SIM.motor_temps = {vex.Ports.PORT2: 61}
        lines = run(self.PATH)
        self.assertIn("PREFLIGHT motor=LB port=2 ok=0 temp=61", lines)
        self.assertEqual(lines[-1], "PREFLIGHT result=NO-GO")

    def test_low_battery_is_no_go(self):
        SIM.battery = 35
        lines = run(self.PATH)
        self.assertEqual(lines[-1], "PREFLIGHT result=NO-GO")
        self.assertIn("Battery: 35% CHARGE ME", SIM.brain_screen)

    def test_missing_motor(self):
        SIM.missing_ports = {vex.Ports.PORT10}
        lines = run(self.PATH)
        self.assertIn("PREFLIGHT motor=RB port=10 ok=0 temp=na", lines)
        self.assertEqual(lines[-1], "PREFLIGHT result=NO-GO")


@unittest.skipUnless(shutil.which("g++"), "g++ not installed")
class TestCppCompiles(unittest.TestCase):
    def test_arcade_drive_cpp(self):
        src = os.path.join(M1, "log-10-real-code", "arcade_drive.cpp")
        result = subprocess.run(
            ["g++", "-std=c++17", "-fsyntax-only", "-Wall", "-Werror",
             "-I", os.path.join(HERE, "cpp"), src],
            capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
