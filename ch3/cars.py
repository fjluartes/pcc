#!/usr/bin/env python
# cars.py: organizing a list
# sorted(): sort a list temporarily (function)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here's the original list:")
print(cars)
print("\nHere's the sorted list:")
print(sorted(cars))
print("\nHere's the original list again:")
print(cars)

# reverse(): print a list in reverse order (method)
cars.reverse()
print(cars)

# sort(): sort a list permanently (method)
cars.sort()
print(cars)
# sort in reverse
cars.sort(reverse=True)
print(cars)

# len(): print length of a list (function)
print(len(cars))
print(cars)
