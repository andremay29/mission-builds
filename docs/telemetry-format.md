# Telemetry format

The rover programs print simple text lines to the VEXcode console. The cyberdeck's [mission screen](../mission-02-cyberdeck/mission-screen/) reads these same lines: pasted in today, streamed live in a later Mission 02 episode.

Each line is a **tag** followed by `key=value` pairs separated by spaces. Values never contain spaces (they use `_` instead).

## PREFLIGHT lines

From [systems_check.py](../mission-02-cyberdeck/preflight/systems_check.py):

```
PREFLIGHT battery=87
PREFLIGHT motor=LF port=1 ok=1 temp=32
PREFLIGHT motor=RB port=10 ok=0 temp=na
PREFLIGHT result=NO-GO
```

| Key | Meaning |
|---|---|
| `battery` | Battery charge, percent |
| `motor` | Short motor ID (LF = left front, RB = right back, …) |
| `port` | Brain port number |
| `ok` | `1` = good, `0` = missing or too hot |
| `temp` | Motor temperature in °C, or `na` if the motor wasn't found |
| `result` | `GO` or `NO-GO` |

## TLM lines

From [mars_mission.py](../mission-01-mars-rover/log-12-mars-mission/mars_mission.py):

```
TLM t=0.0 bat=88 event=launch
TLM t=4.2 bat=88 event=site detail=Jezero_Delta
TLM t=21.7 bat=86 event=complete
```

| Key | Meaning |
|---|---|
| `t` | Seconds since launch |
| `bat` | Battery charge, percent |
| `event` | `launch`, `site`, `abort`, or `complete` |
| `detail` | Extra info, like the site name (`_` for spaces) |

Any line that doesn't start with a known tag is ignored, so ordinary `print()` debugging won't confuse the mission screen.
