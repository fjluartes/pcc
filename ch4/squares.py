#!/usr/bin/env python
# squares.py: generate the first 10 square numbers into a list
# 12 Aug 2018 | fjgl
squares1 = []
for value in range(1, 11):
    square = value**2
    squares1.append(square)
print(squares1)

# without the square temporary variable
squares2 = []
for value in range(1, 11):
    squares2.append(value**2)
print(squares2)

# simple statistics
print(min(squares2))
print(max(squares2))
print(sum(squares2))

# list comprehension
squares3 = [value**2 for value in range(1, 11)]
print(squares3)


