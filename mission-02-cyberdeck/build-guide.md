# Cyberdeck build guide

Four stages, about one weekend each. **Test everything loose on the desk before buying the case or printing anything**, so if something doesn't work you've only spent money on parts you can still use.

Grown-ups: Stage 2 involves a 3D printer and Stage 3 a utility knife. Kids can do lots of this, with an adult for those steps.

## Parts

Prices checked October 2026; they change often.

| Part | About | Why |
|---|---|---|
| Raspberry Pi 5, 4 GB | $85–110 | The computer. 4 GB is plenty for a web browser and VEXcode. |
| Raspberry Pi Touch Display 2 (7-inch) | $82 | The screen. Plugs straight into the Pi. |
| Display cable for Pi 5 | $4 | In case the right one isn't in the screen's box. |
| Raspberry Pi Active Cooler | $11 | Fan and heatsink; the Pi gets warm in a case. |
| Official Pi 27 W USB-C power supply | $13 | Weaker phone chargers cause crashes. |
| 64 GB microSD card, "A2" rated | $15 | Holds the operating system. |
| Mini wireless keyboard with touchpad (Rii i8+ or similar) | $25 | Keyboard and mouse in one. |
| Hard case (Harbor Freight Apache 2800 or similar) | $30 | The rugged shell. |
| 3D-printed screen case, screws, mounting tape | about $15 | Holds the screen in the lid. |

**Budget option:** skip the display and its cable, and show the Pi's screen on an old iPad over Wi-Fi with Raspberry Pi Connect (free). It saves about $86 but depends on Wi-Fi.

**Already have:** a computer to set up the microSD card, the VEX V5 kit (the controller's USB cable is your link to the rover), a small Phillips screwdriver.

## Stage 1: Bring it to life on the desk

### A. Prepare the microSD card

1. Install **Raspberry Pi Imager** (free) from raspberrypi.com on your computer.
2. Put the microSD card in your computer (use an adapter if needed).
3. In Imager choose **Device: Raspberry Pi 5**, **OS: Raspberry Pi OS (64-bit)**, and your card.
4. In the settings screen, set a username and password (write them down), your Wi-Fi, and your time zone.
5. Click **Write** and wait about 10 minutes. Eject the card.

### B. Put the hardware together

1. **Cooler:** peel the thermal-pad backing, push its two pins through the Pi's holes, plug its cable into the port marked **FAN**.
2. **Screen:** lift the latch on one of the Pi's narrow display ports, slide the ribbon cable in fully, press the latch down.
3. **Screen power:** connect the display's two small power wires to the Pi's pins **exactly** as the leaflet in the box shows. Check twice; wrong pins can damage the screen.
4. Plug the keyboard's USB receiver into the Pi. Put the microSD card in the slot underneath.
5. Plug in power last. The Pi turns on by itself.

### C. First start-up

1. If the picture is sideways, open **Menu → Preferences → Screen Configuration**, right-click the screen, and set the **Orientation** to landscape.
2. Open **Terminal** and update everything:

   ```bash
   sudo apt update && sudo apt full-upgrade -y
   ```

3. Restart from the menu.

### D. The big test: can the deck talk to the rover?

1. Open **Chromium** on the Pi and go to **codev5.vex.com**. (Raspberry Pi isn't on VEX's official list of supported devices, so this test tells you if it works before you spend more.)
2. Turn on the V5 Brain and connect it to the Pi with the micro-USB cable from the kit.
3. In VEXcode, click the **Brain icon → Connect** and choose the port with the **lowest** number. The icon turns green.
4. Build a one-block program, `print "Mission control online" on Brain`, then **Download** and **Run**. The words appear on the Brain.
5. **Wireless:** unplug the Brain, plug the **controller** into the Pi instead (controller linked to the Brain), and download again.

**It worked?** Buy the case and move on. **It didn't?** Don't buy the case yet. Fallback: code the rover from your regular computer and use the deck as the on-camera mission screen.

## Stage 2: Print the screen case

The screen needs a frame to hold it in the case lid. A free design does the job: the [Raspberry Pi Touch Display 2 Case on Printables](https://www.printables.com/model/1071718-raspberry-pi-touch-display-2-case). It takes about 3 hours 20 minutes and about 142 g of plastic.

### No 3D printer? Use the library

Many public libraries have 3D printers, often free or a few cents per gram. Search your library's website for "3D printing" or "makerspace", or just call. **Ask these before you go:**

1. What printer do you have, and which file types do you take (STL or 3MF)?
2. Which plastics do you have? (PLA is fine; PETG handles heat a little better.)
3. What does it cost: per gram, per hour, or free?
4. What's the longest print allowed? (This one is about 3.5 hours.)
5. Do I book a time, and do staff run the printer or do I?

**Other options:** an online print service (upload the file, they mail the part), or a ready-made [panel-mount enclosure for Touch Display 2](https://thepihut.com/products/panel-mounting-enclosure-for-raspberry-pi-touch-display-2) with no printing at all.

### Get the files ready

1. Make a free Printables account and open the model page.
2. Download the **"direct tapping"** version (no heat-set inserts; inserts need a soldering iron).
3. Pick the **no mounting holes** variant; it'll be taped into the lid.
4. Copy the files to a USB stick.
5. Read the model's comments for anyone who fit a **Pi 5 with the Active Cooler** (the cooler adds height). If no one mentions it, bring your Pi to compare before printing.

### At the printer

- Ask for **black or dark gray** plastic.
- Supports only under the top of the cable channel ("organic" supports); none for the screw holes or vent.
- When it's done, snap the supports off gently with pliers.

### Fit the screen

1. Lay the screen face-down on a soft towel and set the printed case over it.
2. Fasten it with the M2.5 screws from the display's box (M2.5 × 8 mm screws from a hardware store are easier).
3. Mount the Pi on the back, reconnect the ribbon cable and power wires as in Stage 1.
4. A **right-angle USB-C adapter** (about $8) helps the power cable fit.

## Stage 3: Build it into the case

The screen goes in the **lid**; the keyboard and cables go in the **base**.

```
   LID (opens up)                 BASE
 +----------------------+      +----------------------+
 |                      |      |  [ keyboard pocket ] |
 |   7" SCREEN + PI     |      |                      |
 |   in printed case    |      |  [ cable pocket ]    |
 |                      |      |  [ V5 controller ]   |
 +----------------------+      +----------------------+
          hinge -------- power cable runs across here
```

1. **Test-fit:** set the screen case in the lid and close gently. If the lid foam is in the way, remove that layer.
2. **Mark the spot:** center the screen, slightly toward the hinge, and trace around it.
3. **Mount:** clean both surfaces with rubbing alcohol, use 4 strips of heavy-duty double-sided mounting tape, press for 60 seconds, and wait 24 hours before heavy use.
4. **Breathing room:** keep at least a finger's width of open air around the Pi's fan. Never run the deck with the lid closed.
5. **Base foam:** pluck out pockets for the keyboard, the coiled power supply, and the V5 controller.
6. **Power cable:** run it across the hinge with some slack and clip it to the lid's edge. Don't drill the case.
7. **The look:** a "MISSION CONTROL" label on the lid, a mission patch sticker, some warning labels by the keyboard.

**Before every use:** lid fully open, fan uncovered, cable not pinched.

## Stage 4: Mission control software

On the Pi, open **Terminal** and download this repo:

```bash
git clone https://github.com/andremay29/mission-builds.git
```

Then open the mission screen:

```bash
mission-builds/mission-02-cyberdeck/mission-screen/start-mission-control.sh
```

Details, the pre-flight check, and launching it automatically at start-up: [mission-screen/README.md](mission-screen/README.md).

### The launch routine (same every time)

1. Open the case and plug in power.
2. Plug the V5 controller into the Pi by USB and turn on the rover.
3. Open VEXcode in Chromium and download the mission program wirelessly.
4. Run the pre-flight check and read the result into the mission screen.
5. Tick the checklist, start the countdown, and launch.
