import sys


def calculate(operation, operand1, operand2):
    if operation == "sum":
        return operand1 + operand2
    elif operation == "sub":
        return operand1 - operand2
    elif operation == "mul":
        return operand1 * operand2
    elif operation == "div":
        if operand2 == 0:
            return "Error: Division by zero"
        return operand1 / operand2
    return "Error: Unsupported operation"


def is_valid_number(number_str):
    return number_str.isdigit() or (
        "." in number_str and number_str.replace(".", "", 1).isdigit()
    )


def parse_number(number_str):
    return float(number_str) if "." in number_str else int(number_str)


def get_input(prompt):
    user_input = input(prompt)
    if is_valid_number(user_input):
        return parse_number(user_input)
    else:
        raise ValueError("Error: Invalid input")


validated_operation = ["sum", "sub", "mul", "div"]
if len(sys.argv) == 4:
    operation = sys.argv[1]
    if operation not in validated_operation:
        print("Error: Unsupported operation")
        sys.exit(1)

    operand1_str = sys.argv[2]
    operand2_str = sys.argv[3]

    try:
        if is_valid_number(operand1_str):
            operand1 = parse_number(operand1_str)
        else:
            raise ValueError

        if is_valid_number(operand2_str):
            operand2 = parse_number(operand2_str)
        else:
            raise ValueError

        result = calculate(operation, operand1, operand2)
        print("Output:", result)
    except ValueError:
        print("Error: Invalid input")
else:
    print("Interactive Mode:")
    while True:
        operation = input("Operation: ")
        if operation not in validated_operation:
            print("Error: Unsupported operation")
            continue
        try:
            operand1 = get_input("Operand 1: ")
            operand2 = get_input("Operand 2: ")
            result = calculate(operation, operand1, operand2)
            print("Output:", result)
            break
        except ValueError:
            print("Error: Invalid input")
