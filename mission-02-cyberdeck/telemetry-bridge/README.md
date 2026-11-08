# Telemetry bridge (coming in Mission 02, Log 07)

The goal: rover data on the mission screen **live, while the rover drives**, with no cables and no copy and paste.

The plan:

```
 Rover                                     Cyberdeck
+------------------+   USB    +--------+   Wi-Fi   +-------------------+
| V5 Brain         |--------->| small  |---------->| mission screen    |
| prints TLM lines |  serial  | Pi on  |           | (shows live data) |
+------------------+          | rover  |           +-------------------+
                              +--------+
```

- The rover program already prints `TLM` lines ([format](../../docs/telemetry-format.md)).
- A small computer riding on the rover reads them from the Brain's USB port and forwards them over Wi-Fi.
- The mission screen already understands the lines; it just needs to receive them live instead of pasted.

The code for this lands here when the episode is filmed.
