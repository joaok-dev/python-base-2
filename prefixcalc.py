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
"""
__version__ = "0.1.0"
__author__ = "joaok"

import sys

# Get command line arguments or ask the user for inputs
arguments = sys.argv[1:]

# TODO: Exceptions
# No CLI arguments provided, ask user for inputs
if not arguments:
    operation = input("Operation:")
    operand1 = input("Operand 1:")
    operand2 = input("Operand 2:")
    arguments = [operation, operand1, operand2]
# Verify correct number of CLI arguments, exit if incorrect
elif len(arguments) != 3:
    print("Incorrect number of arguments")
    print("Ex: `sum 5 5`")
    sys.exit(1)

# Extract operation and operands
operation, *operands = arguments

# List of allowed operations
valid_operations = ("sum", "sub", "mul", "div")

# Validate the provided operation, exit if invalid
if operation not in valid_operations:
    print("Invalid Operation")
    print(valid_operations)
    sys.exit(1)

# TODO: While repetition + exceptions
# Empty list to hold validated operands
validated_operands = []

# Validate operands and type-cast them
for operand in operands:
    # Check if operand is a valid number, exit if not
    if not operand.isdigit():
        print(f"Invalid number {operand}")
        sys.exit(1)

    # Type cast to float or int based on the value
    if "." in operand:
        operand = float(operand)
    else:
        operand = int(operand)

    validated_operands.append(operand)  # Append the validated operand to the list

# Extract the validated operands
operand1, operand2 = validated_operands

# TODO: Use function dicts
# Perform the operation based on the provided operator
if operation == "sum":
    result = operand1 + operand2
elif operation == "sub":
    result = operand1 - operand2
elif operation == "mul":
    result = operand1 * operand2
elif operation == "div":
    result = operand1 / operand2  # Note: No zero-division check yet

# Print the calculated result
print(f"The result is {result}")
