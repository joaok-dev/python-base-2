#!/usr/bin/env python3
"""Hello World Multi Languages.

Depending on the language configured in the envoronment, the script displays the 
corresponding message.


Usage:
Ensure the LANG variable is properly configured.

    export LANG=pt_BR

Or provide via the CLI with the --lang argument.
Or the user will have to type.


Execution:
    python3 hello.py
    or
    ./hello.py
"""

__version__ = "0.1.2"
__author__ = "joaok"
__license__ = "Unlicense"

# Import the os and sys modules for environment variable and
# command line argument handling.
import logging
import os
import sys

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger(__name__, log_level)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fmt = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s"
)
ch.setFormatter(fmt)
log.addHandler(ch)

# Initialize a dictionary to hold the command-line arguments.
arguments = {
    "lang": None,
    "count": 1,
}

# Loop through the command line arguments starting from index 1
# (ignoring the script name).
for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error("You need to use `=`, you typed %s, try --key=value: %s", arg, str(e))
        sys.exit(1)

    # Remove leading hyphens and whitespace from the key.
    key = key.lstrip("-").strip()
    # Strip whitespace from the value.
    value = value.strip()

    # Validate the argument key.
    if key not in arguments:
        print("Invalid Argument {key}")
        # Exit the program if the key is not recognized.
        sys.exit()

    # Store the value into the arguments dictionary.
    arguments[key] = value

# Get the language preference from the arguments or fall back
# to the environment variable.
current_language = arguments["lang"]
if current_language is None:
    # TODO: Implement a loop for persistent language setting.
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")

# Trim the language code to first 5 characters (language and region).
current_language = current_language[:5]

# Message dictionary containing greeting messages in multiple languages.
msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_ES": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}
try:
    message = msg[current_language]
except KeyError as e:
    print(f"[ERROR] {str(e)}")
    print(f"Languange invalid, chose from: {list(msg.keys())}")
    sys.exit(1)

# Print the greeting message.
print(message * int(arguments["count"]))
