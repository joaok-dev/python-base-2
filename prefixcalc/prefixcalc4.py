#!/usr/bin/env python
"""Prefix Calculator.

Operation Format:

[operation] [operand1] [operand2]

Supported Operations:
- sum: Addition (+)
- sub: Subtraction (-)
- mul: Multiplication (*)
- div: Division (/)

Usage Examples:
$ prefixcalc.py sum 5 2
Output: 7

$ prefixcalc.py mul 10 5
Output: 50

Interactive Mode:
$ prefixcalc.py
Operation: sum
Operand 1: 5
Operand 2: 4
Output: 9

The results will be saved in `prefixcalc.log`
"""
__version__ = "0.1.0"
__author__ = "joaok"

import os
import sys
from datetime import datetime

# Dictionary for mapping operations to actual Python operations
operation_dict = {
    "sum": lambda x, y: x + y,
    "sub": lambda x, y: x - y,
    "mul": lambda x, y: x * y,
    "div": lambda x, y: x / y,
}

# Get command line arguments from the user
arguments = sys.argv[1:]

# No CLI arguments provided, ask user for inputs
if not arguments:
    operation = input("Operation:")
    operand1 = input("Operand 1:")
    operand2 = input("Operand 2:")
    arguments = [operation, operand1, operand2]
# Verify ocorrect number of CLI arguments, exit if incorret
elif len(arguments) != 3:
    print("Incorrect number of arguments")
    print("Ex: sum 5 5")
    sys.exit(1)

# Extract operation and operands
operation, *operands = arguments

# Validate the provided operation using EAFP, exit if invalid
try:
    operation_func = operation_dict[operation]
except KeyError:
    print("Invalid Operation")
    print(list(operation_dict.keys()))
    sys.exit(1)

# Empty list to hold validated operands
validated_operands = []

# Validate operands using EAFP and type-cast them
for operand in operands:
    try:
        # Try type casting to float first (it will work for intgers too)
        operand = float(operand)
        # If it's actually an integer, cas it to int
        if operand.is_integer():
            operand = int(operand)
    except ValueError:
        print(f"Invalid number {operand}")
        sys.exit(1)

    validated_operands.append(operand)

# Try unpacking operands and perform operation using EAFP
try:
    operand1, operand2 = validated_operands
    result = operation_func(operand1, operand2)
except ValueError:
    print("Error unpacking operands")
    sys.exit(1)
except ZeroDivisionError:
    print("Division by zero is not allowed")
    sys.exit(1)

# File writing using EAFP
path = os.curdir
filepath = os.path.join(path, "prefixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv("USER", "anonymous")

try:
    with open(filepath, "a") as f:
        f.write(f"{timestamp} - {user} - {operation}, {operand1}, {operand2}")
except (FileNotFoundError, PermissionError):
    print("Could not write to log file")

# Print the calculated result
print(f"The result is {result}")
