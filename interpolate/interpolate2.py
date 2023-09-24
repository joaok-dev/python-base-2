import os
import sys

# Try inpacking filename and templatename using EAFP
try:
    filename, templatename = sys.argv[1:]
except ValueError:
    print("Invalid Number of Arguments")
    print("Insert the command with the name of the files.")
    print("Ex: interpolate.py email.txt email_tmpl.txt")
    sys.exit(1)

# Build full file paths
filepath = os.path.join(os.curdir, filename)
templatepath = os.path.join(os.curdir, templatename)

# Read the template using EAFP
try:
    with open(templatepath) as f:
        template = f.read()
except (FileNotFoundError, PermissionError):
    print(f"Error reading template file {templatepath}")

# Process each line in the customer email file using EAFP
try:
    with open(filepath) as f:
        for line in f:
            try:
                # Try unpacking name and email
                name, email = line.strip().split(",")
            except ValueError:
                print(f"Invalid line format: {line.strip()}")
                continue  # Skip to the next iteration

            print(f"Sending email to {email}\n")
            print(
                template.format(
                    name=name,
                    product="pen",
                    text="Writes very well",
                    link="https://coolpens.com",
                    amount=1,
                    price=50.5,
                )
            )
            print("-" * 50)
except (FileNotFoundError, PermissionError):
    print(f" Error reading email file {filepath}")
    sys.exit(1)
