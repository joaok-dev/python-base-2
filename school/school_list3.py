#!/usr/bin/env python
""" Display students reports by activity.

Print the list of children grouped by room who participate in each of the activities.
"""

__version__ = "0.1.0"
__author__ = "joaok"

# Initialize a dictionary for students keyed by name and valued by room
students = {
    "Anthony": "room1",
    "Kevin": "room1",
    "Jennifer": "room1",
    "Angelica": "room1",
    "Sylvia": "room1",
    "Timothy": "room2",
    "Jake": "room2",
    "Connie": "room2",
    "Valerie": "room2",
    "Erin": "room2",
}

# Define the classes and the students attending each class
classes = [
    ("Portuguese", ["Anthony", "Timothy", "Jake", "Jennifer", "Angelica"]),
    ("Chess", ["Kevin", "Jennifer", "Angelica", "Erin", "Valerie", "Connie"]),
    ("Jazz", ["Timothy", "Jake", "Sylvia", "Angelica", "Erin", "Valerie"]),
]

# Loop through each class to find intersecting students from each room
for class_name, class_list in classes:
    class_room1 = list(
        set(class_list)
        & set([student for student, room in students.items() if room == "room1"])
    )
    class_room2 = list(
        set(class_list)
        & set([student for student, room in students.items() if room == "room2"])
    )

    # Output the results
    print()
    print(f"{class_name} room 1 ", class_room1)
    print(f"{class_name} room 2 ", class_room2)
    print("-" * 30)
