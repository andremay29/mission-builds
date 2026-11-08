// A tiny stand-in for VEXcode V5's C++ header, so CI can check that the
// C++ examples compile. It declares only what the examples use; it does not
// drive any hardware.
#pragma once
#include <cstdint>
#include <initializer_list>
#include <vector>

namespace vex {

enum class directionType { fwd, rev };
enum class percentUnits { pct };
enum class timeUnits { msec, sec };
enum class gearSetting { ratio36_1, ratio18_1, ratio6_1 };
enum class controllerType { primary, partner };

const directionType forward = directionType::fwd;
const directionType reverse = directionType::rev;
const percentUnits percent = percentUnits::pct;
const timeUnits msec = timeUnits::msec;
const timeUnits seconds = timeUnits::sec;
const gearSetting ratio18_1 = gearSetting::ratio18_1;
const gearSetting ratio36_1 = gearSetting::ratio36_1;
const gearSetting ratio6_1 = gearSetting::ratio6_1;
const controllerType primary = controllerType::primary;

const int32_t PORT1 = 0, PORT2 = 1, PORT3 = 2, PORT4 = 3, PORT5 = 4, PORT6 = 5, PORT7 = 6,
              PORT8 = 7, PORT9 = 8, PORT10 = 9, PORT11 = 10, PORT12 = 11, PORT13 = 12,
              PORT14 = 13, PORT15 = 14, PORT16 = 15, PORT17 = 16, PORT18 = 17, PORT19 = 18,
              PORT20 = 19, PORT21 = 20;

inline void wait(double, timeUnits) {}

class screen {
 public:
  void clearScreen() {}
  void setCursor(int32_t, int32_t) {}
  template <typename... T> void print(T...) {}
  void newLine() {}
};

class brain {
 public:
  screen Screen;
};

class axis {
 public:
  int32_t position() const { return 0; }
};

class button {
 public:
  bool pressing() const { return false; }
};

class controller {
 public:
  controller() {}
  explicit controller(controllerType) {}
  axis Axis1, Axis2, Axis3, Axis4;
  button ButtonA, ButtonB, ButtonX, ButtonY, ButtonL1, ButtonL2, ButtonR1, ButtonR2;
  screen Screen;
};

class motor {
 public:
  motor(int32_t, gearSetting, bool) {}
  void spin(directionType, double, percentUnits) {}
  void stop() {}
};

class motor_group {
 public:
  template <typename... M> motor_group(M&... motors) : count_(sizeof...(motors)) {}
  void spin(directionType, double, percentUnits) {}
  void stop() {}

 private:
  int count_;
};

}  // namespace vex
