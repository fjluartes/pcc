#!/usr/bin/env python
# pets.py: removing instances of an item in a list
# 21 Aug 2018 | fjgl
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
