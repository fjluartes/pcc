#!/usr/bin/env python
# stages_of_life.py: Exercise 5-6
# 13 Aug 2018 | \251 fjgl
# age = 1
# age = 2
# age = 4
# age = 13
# age = 20
age = 65

if age < 2:
    print("You are a baby.")
elif age < 4:
    print("You are a toddler.")
elif age < 13:
    print("You are a kid.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
elif age >= 65:
    print("You are an elder.")
