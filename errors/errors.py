#!/usr/bin/env python
import os
import sys

# LBYL - LOOK BEFORE YOU LEAP

if os.path.exists("names.txt"):
    print("The file exists.")
    input("...")  # Race Condition
    names = open("names.txt").readline()
else:
    print("[Error] File names.txt not found")
    sys.extit(1)

if len(names) >= 3:
    print(names[2])
else:
    print("[Error] Missing name in the list.")
    sys.exit(1)
