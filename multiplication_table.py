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

for i in base:
    print("Multiplication Table of:", i)
    print()
    for j in base:
        result = i * j
        print(result)
    print()
    print()
