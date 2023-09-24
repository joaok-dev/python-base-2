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

cmds = ("read", "new")
path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print(f"You must specifu a subcommand {cmds}")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")
    sys.exit(1)

try:
    if arguments[0] == "read":
        try:
            with open(filepath, "r") as file_:
                for line in file_:
                    try:
                        title, tag, text = line.split("\t")
                        if tag.lower() == arguments[1].lower():
                            print(f"title: {title}")
                            print(f"text: {text}")
                            print("-" * 30)
                            print()
                    except ValueError:
                        print(f"Invalid line format: {line.strip()}")
        except FileNotFoundError:
            print(f"File {filepath} not found.")

    if arguments[0] == "new":
        try:
            title = arguments[1]
        except IndexError:
            print("Title not provided.")
            sys.exit(1)

        text = [
            f"{title}",
            input("tag:").strip(),
            input("text:\n").strip(),
        ]

        # Attempt to write to the file
        with open(filepath, "a") as file_:
            file_.write("\t".join(text) + "\n")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
