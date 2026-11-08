// ---------------------------------------------------------------
//  Mission Builds HQ | Mission 01, Log 10: Same rover, real code
//  Runs in VEXcode V5 (C++): codev5.vex.com or the VEXcode app
//
//  The exact same arcade drive as Log 07's Python version, written
//  in C++, the language most competition teams and a lot of real
//  robots use. Compare them line by line: the ideas are identical,
//  only the punctuation changes.
//
//  How to use: make a new C++ project, don't add any devices in the
//  Devices menu, and replace everything in main.cpp with this file.
//  If VEXcode says "Brain" is defined twice, delete the brain line
//  in the ROBOT CONFIG section below.
// ---------------------------------------------------------------
#include "vex.h"
#include <cstdlib>

using namespace vex;

// ---------- ROBOT CONFIG: change these to match YOUR build ----------
brain Brain;
controller Controller1 = controller(primary);

motor LeftFront = motor(PORT1, ratio18_1, false);
motor LeftBack = motor(PORT2, ratio18_1, false);
motor RightFront = motor(PORT9, ratio18_1, true);   // reversed: faces the other way
motor RightBack = motor(PORT10, ratio18_1, true);

motor_group LeftDrive = motor_group(LeftFront, LeftBack);
motor_group RightDrive = motor_group(RightFront, RightBack);

const int DEADBAND = 5;          // ignore tiny stick wiggles below this
const double TURTLE_SCALE = 0.5; // hold R1 for half speed
// ---------------------------------------------------------------------

// Treat tiny stick movements as zero, so the rover doesn't creep.
int applyDeadband(int value) {
  if (std::abs(value) < DEADBAND) {
    return 0;
  }
  return value;
}

// Keep a speed between -100 and 100 percent.
double clampPercent(double value) {
  if (value > 100) return 100;
  if (value < -100) return -100;
  return value;
}

int main() {
  Brain.Screen.clearScreen();
  Brain.Screen.setCursor(1, 1);
  Brain.Screen.print("MISSION BUILDS | ROVER ONLINE");
  Controller1.Screen.print("ROVER ONLINE");

  while (true) {
    int forwardInput = applyDeadband(Controller1.Axis3.position());
    int turnInput = applyDeadband(Controller1.Axis1.position());
    double scale = Controller1.ButtonR1.pressing() ? TURTLE_SCALE : 1.0;

    double leftSpeed = clampPercent(forwardInput + turnInput) * scale;
    double rightSpeed = clampPercent(forwardInput - turnInput) * scale;

    LeftDrive.spin(forward, leftSpeed, percent);
    RightDrive.spin(forward, rightSpeed, percent);

    wait(20, msec);  // check the sticks 50 times a second
  }
}
