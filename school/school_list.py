#!/usr/bin/env python
""" Display students reports by activity.

Print the list of children grouped by room who participate in each of the activities.
"""

__version__ = "0.1.0"
__author__ = "joaok"

# Initialize lists for students in room1 and room2
room1 = ["Anthony", "Kevin", "Jennifer", "Angelica", "Sylvia"]
room2 = ["Timothy", "Jake", "Connie", "Valerie", "Erin"]

# Define the classes and the students attending each class
classes = [
    ("Portuguese", ["Anthony", "Timothy", "Jake", "Jennifer", "Angelica"]),
    ("Chess", ["Kevin", "Jennifer", "Angelica", "Erin", "Valerie", "Connie"]),
    ("Jazz", ["Timothy", "Jake", "Sylvia", "Angelica", "Erin", "Valerie"]),
]

# Loop through each class
for class_name, class_list in classes:
    class_room1 = []
    class_room2 = []

    # Loop through each student in the class to find their room
    for student in class_list:
        if student in room1:
            class_room1.append(student)
        elif student in room2:
            class_room2.append(student)

    # Output the results
    print()
    print(f"{class_name} room 1 ", class_room1)
    print(f"{class_name} room 2 ", class_room2)
    print("-" * 30)
