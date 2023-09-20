#!/usr/bin/env python
""" Display students reports by activity.

Print the list of children grouped by room who participate in each of the activities.
"""

__version__ = "0.1.0"
__author__ = "joaok"

# Data
room1 = ["Anthony", "Kevin", "Jennifer", "Angelica", "Sylvia"]
room2 = ["Timothy", "Jake", "Connie", "Valerie", "Erin"]

# Grouping classes into tuples with their respective names
classes = [
    ("Portuguese", ["Anthony", "Timothy", "Jake", "Jennifer", "Angelica"]),
    ("Chess", ["Kevin", "Jennifer", "Angelica", "Erin", "Valerie", "Connie"]),
    ("Jazz", ["Timothy", "Jake", "Sylvia", "Angelica", "Erin", "Valerie"]),
]

# Iterating through each class
for class_name, class_list in classes:
    class_room1 = []
    class_room2 = []

    # Iterating through each student in the current class
    for student in class_list:
        # Check which room the student belongs to and add to the corresponding list
        if student in room1:
            class_room1.append(student)
        elif student in room2:
            class_room2.append(student)

    # Printing the results
    print()
    print(f"{class_name} room 1 ", class_room1)
    print(f"{class_name} room 2 ", class_room2)
    print("-" * 30)
