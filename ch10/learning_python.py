#!/usr/bin/env python
# learning_python.py: Exercise 10-1
# 29 Aug 2018 | fjgl
filename = 'learning_python.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
print("")

with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.strip())
print("")

for line in lines:
    print(line.strip())
