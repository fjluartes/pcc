#!/usr/bin/env python
# pi_string.py: working with file's contents
# 29 Aug 2018 | fjgl
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
