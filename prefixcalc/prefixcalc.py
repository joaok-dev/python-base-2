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

#!/usr/bin/env python
import logging
import os
import sys

# Logging Setup
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.getLogger(__name__)
log.setLevel(log_level)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fmt = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s"
)
ch.setFormatter(fmt)
log.addHandler(ch)

# Get command line arguments or ask the user for inputs
arguments = sys.argv[1:]

# No CLI arguments provided, ask user for inputs
if not arguments:
    operation = input("Operation: ")
    operand1 = input("Operand 1: ")
    operand2 = input("Operand 2: ")
    arguments = [operation, operand1, operand2]

elif len(arguments) != 3:
    log.error("Incorrect number of arguments. Ex: `sum 5 5`")
    sys.exit(1)

operation, *operands = arguments

# List of allowed operations
valid_operations = ("sum", "sub", "mul", "div")

if operation not in valid_operations:
    log.error(f"Invalid operation. Allowed operations are: {valid_operations}")
    sys.exit(1)

# Validate operands and type-cast them
validated_operands = []
for operand in operands:
    if not operand.isdigit():
        log.error(f"Invalid number {operand}")
        sys.exit(1)

    if "." in operand:
        operand = float(operand)
    else:
        operand = int(operand)

    validated_operands.append(operand)

try:
    operand1, operand2 = validated_operands
except ValueError as e:
    log.error(str(e))
    sys.exit(1)

# Perform the operation
try:
    if operation == "sum":
        result = operand1 + operand2
    elif operation == "sub":
        result = operand1 - operand2
    elif operation == "mul":
        result = operand1 * operand2
    elif operation == "div":
        result = operand1 / operand2  # Note: No zero-division check yet
except ZeroDivisionError:
    log.error("Division by zero attempted.")
    sys.exit(1)

log.info(f"{operation}, {operand1}, {operand2} = {result}")

# Output the calculated result
print(f"The result is {result}")
