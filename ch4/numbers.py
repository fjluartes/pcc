#!/usr/bin/env python
# numbers.py: making numerical lists
# 12 Aug 2018 | fjgl
# range(): generates a series of number (function)
# end value is not included in count
for value in range(1, 6):
    print(value)

# list(): create a list (function)
numbers = list(range(1, 6))
print(numbers)

# even_numbers: skip numbers in a given range using range()
even_numbers = list(range(2, 11, 2))
print(even_numbers)
