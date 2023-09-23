"""Notepad

$ notes.py new "My note"
tag: tech
text: 
General anotation about tech carrer

$ notes.py read --tag=tech
...
...

"""
__version__ = "0.1.0"
__author__ = "joaok"

import os
import sys

path = os.curdir
fiilepath = os.path.join(path, "notes.txt")

cmds = ["read", "new"]

arguments = sys.argv[1:]

if not arguments:
    print("Invalid usage")
    sys.exit(1)

validated_arguments = ["new", "read"]

if arguments not in validated_arguments:
    print("Invalid Argument")
    sys.exit(1)

if arguments[0] == "read":
    ...

if arguments[0] == "new":
    ...
