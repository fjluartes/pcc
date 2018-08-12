#!/usr/bin/env python
# dimensions.py: tuples
# 12 Aug 2018 | fjgl
# lists are [], tuples are ()
# tuples are lists that cannot be changed (aka immutable)
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# elements in a tuple cannot be changed
# dimensions[0] = 250

# writing over a tuple: assign new values to the entire tuple
print("Original dimensions:")
for dim in dimensions:
    print(dim)

dimensions = (400, 100)
print("\nModified dimensions:")
for dim in dimensions:
    print(dim)

