#!/usr/bin/env python
# greeter.py: int() function (converts string to int)
# 20 Aug 2018 | fjgl
height = input("How tall are you in inches? ")
height = int(height)

if height >= 36:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
