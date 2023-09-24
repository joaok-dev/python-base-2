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

path = os.curdir
fiilepath = os.path.join(path, "notes.txt")

cmds = ["read", "new"]

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print(f"you must specify subcomand {cmds}")
    sys.exit(1)


if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")

if arguments[0] == "new":
    title = arguments[1]  # TODO: Handle Exception
    text = [
        f"{title}",
        input("tag: ").strip(),
        input("text: \n").strip(),
    ]
    #
    with open(fiilepath, "a") as file_:
        file_.write("\t".join(text) + "\n")

if arguments[0] == "read":
    for line in open(fiilepath):
        title, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"Title: {title}")
            print(f"Text: {text}")
            print("-" * 30)
