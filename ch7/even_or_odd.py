#!/usr/bin/env python
# even_or_odd.py: modulo operator
# 20 Aug 2018 | fjgl
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")