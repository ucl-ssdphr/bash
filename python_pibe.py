#!/usr/bin/python
import sys

for nr, line in enumerate(sys.stdin):
    mystring = str(nr) + ": " + line
    sys.stdout.write(mystring)


