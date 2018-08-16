#!/usr/bin/env python
# amusement_park.py: if-elif-else program
# 16 Aug 2018 | fjgl
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
    
print("Your admission cost is $" + str(price) + ".")
