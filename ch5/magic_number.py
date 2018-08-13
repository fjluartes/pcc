#!/usr/bin/env python
# magic_number.py: checking inequality of numbers
# 13 Aug 2018 | fjgl
answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")

# checking multiple conditions
# using and
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 and age_1 <= 21)

# using or
print(age_0 >= 21 or age_1 >= 21)
print(age_0 <= 21 or age_1 >= 21)
