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

__version__ = "0.1.2"
__author__ = "joaok"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_ES": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

print(msg[current_language])
