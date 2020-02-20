#!/bin/python

import sys
import re

time = raw_input().strip()

match = re.search("([0-9]{2}):([0-9]{2}):([0-9]{2})(AM|PM)", time)

hours = int(match.group(1))
mins = match.group(2)
secs = match.group(3)
a = match.group(4)

if a == "PM" and hours < 12:
    hours += 12
elif a == "AM" and hours == 12:
    hours = 0

print str(hours).zfill(2) + ":" + mins.zfill(2) + ":" + secs.zfill(2)