# EMU

This is the culmination of a really boarding weekend. I started by building an
intcode computer and ended up with something a bit more complex.

I don't believe this has any value other then my own entertainment.

For my own memory:

```
PYTHONPATH=emu python3 emu/eu.py
```

## Remaining

This I should probably do are: 

- Create a loader that can load ROM and RAM from a file or files
- Create a assember because writing it by hand sucks.
- Create peripheral to wire up with the IO bus
- Create a control unit that will step each peripheral including the EU
- Test memory I/O and the stack

Things that sound interesting

- Add an interrupt handler to the EU.
- Add context switching (backup core to ram)
- Create a gnu C dialect for my assembly flavor
- IDK, write a OS?

