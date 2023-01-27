#!/usr/bin/env python3

"""
Inhibit from sleep mode (but allow monitor to go off)
"""

import caffeine.inhibitors
from caffeine.inhibitors import *



inhibitors = [
             GnomeInhibitor(),
             XdgPowerManagmentInhibitor(),
#             XssInhibitor(),
#             XorgInhibitor(),
#             XautolockInhibitor(),
#             XfceInhibitor(),
             XidlehookInhibitor(),
#             XdgScreenSaverInhibitor(),
#             DpmsInhibitor(),
         ]

for obj in inhibitors:
    try:
        obj.inhibit()
    except Exception as exc:
        print("Error:", exc)
    else:
        print("Success:", obj)


# inhibitors = []

for name, cls in {}.items():  #  vars(caffeine.inhibitors).items():
    if cls is BaseInhibitor:
        continue
    if not isinstance(cls, type):
        continue
    if not issubclass(cls, BaseInhibitor):
        continue
    print(name)
    obj = cls()
    try:
        obj.inhibit()
    except Exception as exc:
        print("Error:", exc)
    else:
        print("Success:", obj)
    inhibitors.append(obj)


print("Loop...")
import time
while True:
    time.sleep(1)
