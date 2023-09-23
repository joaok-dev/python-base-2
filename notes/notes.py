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

arguments = sys.argv[1:]
user_input = arguments[0]

validated_user_input = ["new", "read"]
if user_input not in validated_user_input:
    print("Invalid Option")
    sys.exit(1)

elif user_input == "new":
    note_title = input("Note title: ")
    note_content = input("Type your note: ")

    path = os.curdir
    filepath = os.path.join(path, note_title + ".txt")

    with open(filepath, "a") as n:
        n.write(note_content)

elif user_input == "read":
    user_tag = arguments[1]
    tag = user_tag.rsplit("=")[1]
    ...
