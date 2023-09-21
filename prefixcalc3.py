#!/usr/bin/env python

import sys

arguments = sys.argv[1:]

if len(arguments) == 0:
    operation = input("Choose a operation: ")
    operand1 = int(input("Choose the first number: "))
    operand2 = int(input("Choose the second number :"))
    arguments = [operation, operand1, operand2]
elif len(arguments) == 3:
    operation = arguments[0]
    operand1 = int(arguments[1])
    operand2 = int(arguments[2])
else:
    print("Invalid Number of Arguments")
    sys.exit(1)

valid_operations = ["sum", "sub", "mul", "div"]
result = None

if operation not in valid_operations:
    print(f"Invalid Operation `{operation}`")
    sys.exit(1)

if operation == "sum":
    result = operand1 + operand2
elif operation == "sub":
    result = operand1 - operand2
elif operation == "mul":
    result = operand1 * operand2
elif operation == "div":
    result = operand1 / operand2

print(f"The output is {result}")
