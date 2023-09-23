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

# Capture command-line arguments
command_line_args = sys.argv[1:]

# Check if at least one command is provided
if len(command_line_args) < 1:
    print("Error: No command provided. Use 'new' or 'read'.")
    sys.exit(1)  # Exit the program with an error status

# Capture the command ('new' or 'read')
command = command_line_args[0]

# Logic for 'new' command
if command == "new":
    # Check if the title for the note is provided
    if len(command_line_args) < 2:
        print("Error: Title is required for new notes.")
    else:
        # Capture the note's title, tag, and text
        note_title = command_line_args[1]
        note_tag = input("Enter the tag: ")
        note_text = input("Enter the text: ")

        # Create a new file with the note title as the filename
        filename = f"{note_title}.txt"

        # Open the file and write the tag and text using 'with open' for resource management
        with open(filename, "a") as note_file:
            note_file.write(f"Tag: {note_tag}\n")
            note_file.write(f"Text: {note_text}")

# Logic for 'read' command
elif command == "read":
    # Initialize variables to None
    tag = None
    note_name = None

    # Check if additional arguments are provided
    if len(command_line_args) > 1:
        third_arg = command_line_args[1]

        # Capture the tag if '--tag' is provided
        if "--tag" in third_arg:
            tag = third_arg.split("=")[1]

        # Otherwise, capture the note name
        else:
            note_name = third_arg

    # List all .txt files in the current directory
    filenames = [f for f in os.listdir(os.curdir) if f.endswith(".txt")]

    # Read each note file
    for filename in filenames:
        with open(filename, "r") as note_file:
            content = note_file.read()

            # If a tag is specified, show notes with that tag
            if tag:
                if f"Tag: {tag}" in content:
                    print(f"--- {filename} ---")
                    print(content)
            # If a note name is specified, show that specific note
            elif note_name:
                if note_name in filename:
                    print(f"--- {filename} ---")
                    print(content)
                    break  # Stop after finding and displaying the note

# If an invalid command is entered
else:
    print("Error: Invalid command. Use 'new' or 'read.")
