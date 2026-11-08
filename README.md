# Mission Builds HQ

**Build it. Code it. Launch it.** This is the code for every project on the Mission Builds HQ channel, so you can follow along at home, copy it, change it, and make it yours.

[![Tests](https://github.com/andremay29/mission-builds/actions/workflows/tests.yml/badge.svg)](https://github.com/andremay29/mission-builds/actions/workflows/tests.yml)

Mission Builds HQ is a STEAM build channel by Andre May, an Army veteran turned software engineer who is building robots in public and learning space along the way. It's made for **kids and grown-ups**: every project starts simple and has a "level up" for anyone who wants to go deeper.

Find the channel at **@missionbuildshq** on YouTube, TikTok, and Instagram.

## Pick your track

| | Cadet track | Engineer track |
|---|---|---|
| **Who it's for** | New coders, kids about 8 and up, anyone who's never coded | Teens and adults, or cadets ready for more |
| **How you code** | Drag-and-drop **Blocks** in VEXcode | **Python** and **C++**, the same languages real engineers use |
| **Where to start** | Each log's `README` has a block-by-block recipe | Open the `.py` and `.cpp` files |

Same robot, same programs. In VEXcode you can build with Blocks, then switch to Python or C++ when you're ready. Log 10 shows the exact same program three ways.

## The missions

| Mission | What we build | Status |
|---|---|---|
| [Mission 01: Mars Rover](mission-01-mars-rover/) | A six-wheel Perseverance-style rover from a VEX V5 kit, programmed in VEXcode | Now airing |
| [Mission 02: Cyberdeck](mission-02-cyberdeck/) | A Raspberry Pi "mission control" computer in a rugged case, then linking it to the rover | After Mission 01 |

## How to use this code

1. **No robot yet?** Start with [Log 02](mission-01-mars-rover/log-02-simulator/). It runs in VEXcode VR, a free robot simulator in your web browser.
2. **Have a VEX V5 kit?** Open VEXcode V5 ([codev5.vex.com](https://codev5.vex.com) in Chrome, or the VEXcode app), start a new Python or C++ project, and paste in the program from the log you're on.
3. **Change the ROBOT CONFIG section** at the top of each program so the motor ports match your build.

Step-by-step setup: [docs/getting-started.md](docs/getting-started.md).

## Safety first (grown-ups, please read)

- Lift the rover off the table (or hold it) the first time you run a new program.
- VEX batteries and Raspberry Pi power supplies: use the official chargers only.
- Hot glue guns, hobby knives, and 3D printers need an adult nearby.

## Testing

Every robot program here is tested on a computer before it goes on a robot, using a stand-in for the VEX library ([tests/](tests/)):

```bash
python -m unittest discover -s tests -v
```

GitHub runs these tests automatically on every change (the badge at the top). The cyberdeck's mission screen has a browser test too: `node tests/mission_screen_test.js` (needs Node and Playwright).

The programs are tested against that stand-in, not yet on the finished rover. Each log's folder is updated after its episode is filmed, with anything that changed on the real robot.

## Questions and ideas

Open an [issue](https://github.com/andremay29/mission-builds/issues) if something doesn't work or you built something cool with it. Please read the [code of conduct](CODE_OF_CONDUCT.md) first; kids use this space too.

## License

The code is free to use under the [MIT License](LICENSE). The Mission Builds HQ name and logo aren't covered by the license. VEX, VEXcode, and V5 are trademarks of Innovation First, Inc.; LEGO® is a trademark of the LEGO Group; Raspberry Pi is a trademark of Raspberry Pi Ltd. This project isn't affiliated with or endorsed by any of them.
