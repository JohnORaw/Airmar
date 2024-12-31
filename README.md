# Airmar
Scripts to read and configure Airmar transducers.

[Detailed documentation](/docs/SUMMARY.md) resides in the /docs directory and is maintained through GITBOOK.


To test serial output from the RPi, try 

```
(stty 4800 -echo -icrnl; cat) </dev/ttyS0
```
