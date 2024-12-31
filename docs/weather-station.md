# Weather Station

The AIRMAR weather stations are solid and rugged but very expensive. They use ultrasonics rather than a rotating anemometer, so they are not as delicate for the conditions on the NW coast of Ireland.

This script was written to extract data from NMEA0183 serial output on RS232 from a Airmar Weather Station 110WX

The hardware is a RPi4 with a serial HAT connceted to ttyS0.

When running, raw NMEA is saved to ./logs

This version is currently readonly, I will add control and config as needed and has only been tested on the RPi. Version information is:

```
uname -a
Linux RPi4-AirmarWX1 6.6.62+rpt-rpi-v8 #1 SMP PREEMPT Debian 1:6.6.62-1+rpt1 (2024-11-25) aarch64 GNU/Linux
```

Next steps: Figure out and code the UI, probably a web GUI
