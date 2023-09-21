import os
import sys

# Check the number of arguments and assign filenames accordingly
arguments = sys.argv
if len(arguments) == 1:
    print("Email list and email template not found.")
    print("Insert the command with the name of the files.")
    print("Ex: interpolate.py email.txt email_tmpl.txt")
    sys.exit(1)
elif len(arguments) != 3:
    print("Invalid Number of Arguments")
    print("Insert the command with the name of the files.")
    print("Ex: interpolate.py email.txt email_tmpl.txt")
    sys.exit(1)

filename, templatename = arguments[1], arguments[2]

# Build full file paths
filepath = os.path.join(os.curdir, filename)
templatepath = os.path.join(os.curdir, templatename)

# Read the template only once
with open(templatepath) as f:
    template = f.read()

# Process each line in the customer email file
with open(filepath) as f:
    for line in f:
        name, email = line.strip().split(",")  # strip to remove trailing newline

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
