#!/usr/bin/env python
# ten.py: Exercise 7-3
# 20 Aug 2018 | fjgl
number = input("Enter a number: ")
number = int(number)

if number % 10 == 0:
    print("\nThe number " + str(number) + " is divisible by 10.")
else:
    print("\nThe number " + str(number) + " is not divisible by 10.")
