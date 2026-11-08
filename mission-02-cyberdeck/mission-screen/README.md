# Mission screen

The cyberdeck's mission control display: one web page that works with no internet.

- **Mission clock:** pick a countdown (5–60 s), start it, hold it, resume it. After liftoff it counts up (T+).
- **Pre-flight checklist:** tick each item. The banner turns **GO FOR LAUNCH** when everything is ticked and the rover's systems check passed.
- **Rover status:** battery, each motor's temperature, and the GO / NO-GO result from the systems check.
- **Mission log:** a timestamped record of everything that happened.

| Key | Does |
|---|---|
| Space | Start, hold, or resume the countdown |
| R | Reset the clock |
| F | Full screen |

## Open it

On the cyberdeck (after `git clone`, see the [build guide](../build-guide.md)):

```bash
~/mission-builds/mission-02-cyberdeck/mission-screen/start-mission-control.sh
```

On any other computer, just double-click `index.html`.

## Feed it rover data

1. Plug the rover's Brain into the deck by USB.
2. In VEXcode, connect the Brain and open the console (**Connect User / Console Serial Port**, the port with the **highest** number).
3. Run [`../preflight/systems_check.py`](../preflight/systems_check.py) on the rover.
4. Copy the `PREFLIGHT` lines from the console, paste them into **Rover data**, and press **Read**.

Lines from [`mars_mission.py`](../../mission-01-mars-rover/log-12-mars-mission/mars_mission.py) (`TLM …`) work the same way and fill in the mission log. In the last Mission 02 episode this happens live, with no copy and paste.

## Start it automatically when the deck turns on

On Raspberry Pi OS with the **labwc** desktop (the default since late 2024), add the launcher to the autostart file:

```bash
mkdir -p ~/.config/labwc
echo "$HOME/mission-builds/mission-02-cyberdeck/mission-screen/start-mission-control.sh &" >> ~/.config/labwc/autostart
```

Restart, and the deck boots straight into mission control. To undo it, delete that line from `~/.config/labwc/autostart`.

## Make it yours

Edit `DEFAULT_CHECKLIST` near the top of the script section in `index.html` to change the checklist. The colors are at the top of the `<style>` section.
