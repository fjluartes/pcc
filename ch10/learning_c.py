#!/usr/bin/env python
# learning_c.py: Exercise 10-2
# 29 Aug 2018 | fjgl
filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    new_line = line.replace('Python', 'C')
    print(new_line.strip())
