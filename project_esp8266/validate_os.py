# SD card
import os


# test is able to access uname named tuple
if os.uname().release == "1.13.0" and os.uname().version < "v1.13-103": # type: ignore # FIXME override stdlib
    raise NotImplementedError("MicroPython 1.13.0 cannot be stubbed")

u = os.uname() # type: ignore # FIXME override stdlib
print( u.sysname)
print( u.nodename)
print( u.release)
print( u.machine)
print( u.version)

