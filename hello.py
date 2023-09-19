#!/usr/bin/env python3
"""Hello World Multi Languages.

Depending on the language configured in the envoronment, the script displays the 
corresponding message.

Usage:
Ensure the LANG variable is properly configured.

    export LANG=pt_BR

Execution:
    python3 hello.py
    or
    ./hello.py
"""

__version__ = "0.1.0"
__author__ = "joaok"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_ES":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"

print(msg)
