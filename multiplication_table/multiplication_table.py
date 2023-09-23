#!/usr/bin/env python
"""Print the multiplication table from 1 to 10.

Multiplication Table 1

1
2
3
...
----------

Multiplication Table 2
2
4
6
...
---------

"""

__version__ = "0.1.0"
__author__ = "joaok"

base = list(range(1, 11))
result = None

for n1 in base:
    print(f"Multiplication Table of: {n1}")
    print()
    for n2 in base:
        result = n1 * n2
        print(f"{n1} x {n2} = {result}")
    print()
    print()
