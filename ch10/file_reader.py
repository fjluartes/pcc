#!/usr/bin/env python
# file_reader.py: reading an entire file
# 29 Aug 2018 | fjgl
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
