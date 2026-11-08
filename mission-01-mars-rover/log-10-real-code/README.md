# Log 10: Same rover, real code

Everything so far could be built with Blocks. This log shows that the rover's brain speaks real programming languages too: the same drive program in **Blocks**, **Python**, and **C++**.

| Version | File |
|---|---|
| Blocks | Recipe in [Log 07](../log-07-first-drive/README.md#cadet-track-blocks) |
| Python | [`../log-07-first-drive/arcade_drive.py`](../log-07-first-drive/arcade_drive.py) |
| C++ | [`arcade_drive.cpp`](arcade_drive.cpp) |

Open the Python and C++ files side by side. Every line in one has a twin in the other; the ideas are identical and only the punctuation changes. There's a line-by-line comparison table in [docs/blocks-python-cpp.md](../../docs/blocks-python-cpp.md).

## Trying the C++ version

1. In VEXcode V5: **File → New Text Project → C++**. Don't add devices in the Devices menu.
2. Replace everything in `main.cpp` with [`arcade_drive.cpp`](arcade_drive.cpp).
3. If VEXcode says `Brain` is defined twice, delete the `brain Brain;` line in ROBOT CONFIG (your project already has one).
4. Download and run. It should drive exactly like the Python version.

## Moving from Blocks to text, gently

VEXcode's **Switch blocks** show a block as editable Python while you're still in a Blocks project. Right-click any block → **Convert Block to Switch Block**.

## Where this goes next

The same skills carry into tools outside VEX. Teams that outgrow VEXcode often move to VS Code with the VEX extension, or to community tools like PROS (C++) for competition robots.
