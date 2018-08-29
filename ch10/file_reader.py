#!/usr/bin/env python
# file_reader.py: reading an entire file
# 29 Aug 2018 | fjgl
filename = 'pi_digits.txt'

# reading an entire file
# rstrip(): remove whitespace
#with open(filename) as file_object:
#    contents = file_object.read()
#    print(contents.rstrip())

# reading line by line
#with open(filename) as file_object:
#    for line in file_object:
#        print(line.rstrip())

# making list of lines from a file
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
