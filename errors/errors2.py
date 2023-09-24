#!/usr/bin/env python3
import sys

# EAFP - EASY ASK FORGIVENESS THAN PERMISSION

try:
    names = open("names.txt").readlines()  # FileNotFoundError
except FileNotFoundError as e:
    print(f"{str(e)}")
    sys.exit(1)
else:
    print("Sucess!")
finally:
    print("This will pear always.")

try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)
