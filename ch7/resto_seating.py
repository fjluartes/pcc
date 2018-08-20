#!/usr/bin/env python
# resto_seating.py: Exercise 7-2
# 20 Aug 2018 | fjgl
dinner_group = input("How many are you in the dinner group? ")
dinner_group = int(dinner_group)

if dinner_group > 8:
    print("\nSorry, your group have to wait for a table.")
else:
    print("\nYour table is ready.")
