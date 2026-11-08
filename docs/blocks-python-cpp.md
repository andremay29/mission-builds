# One program, three languages

VEXcode V5 lets you code the same robot in **Blocks**, **Python**, or **C++**. Blocks are perfect for learning the ideas. Python and C++ are the same languages used by working engineers: Python is everywhere in science, data, and AI, and C++ runs game engines, cars, and a lot of robots. NASA JPL's open-source flight software framework, [F´ (F Prime)](https://fprime.jpl.nasa.gov/overview/), is built in C++ and flew on the Ingenuity Mars helicopter.

Here's the "drive with the controller" program from [Log 07](../mission-01-mars-rover/log-07-first-drive/) and [Log 10](../mission-01-mars-rover/log-10-real-code/), side by side.

| Idea | Blocks | Python | C++ |
|---|---|---|---|
| Repeat forever | `forever` | `while True:` | `while (true) { … }` |
| Read the left stick | `Controller1 Axis3 position` | `controller_1.axis3.position()` | `Controller1.Axis3.position()` |
| Add two numbers | `( ) + ( )` | `forward + turn` | `forwardInput + turnInput` |
| Make a decision | `if … then … else` | `x if condition else y` | `condition ? x : y` |
| Spin the wheels | `spin LeftDrive forward` | `left_drive.spin(FORWARD, speed, PERCENT)` | `LeftDrive.spin(forward, speed, percent);` |
| Wait a moment | `wait 0.02 seconds` | `wait(20, MSEC)` | `wait(20, msec);` |
| Leave a note | (comment block) | `# a comment` | `// a comment` |

**What changes between them:** mostly punctuation. Python uses indentation (spaces at the start of a line) to group code. C++ uses `{ }` braces and ends lines with `;`, and it wants you to say what kind of value each variable holds (`int`, `double`).

**What doesn't change:** the thinking. Read the sticks, mix them into left and right speeds, spin the motors, repeat 50 times a second. Once you can do it in Blocks, you already know the program; Python and C++ are new ways to write it down.

## A bridge: Switch blocks

VEXcode V5 has **Switch blocks**: right-click a block and choose **Convert Block to Switch Block** to see it as Python you can type into, still inside your Blocks project. It's a gentle way to move from Blocks to Python one block at a time. ([VEX's guide to Switch blocks](https://kb.vex.com/hc/en-us/articles/29201524290452-Using-Switch-Blocks-to-Transition-from-Blocks-to-Text-Based-Coding))
