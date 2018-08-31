#!/usr/bin/env python
# cats_and_dogs.py: Exercises 10-8, 10-9
# 31 Aug 2018 | fjgl
def read_files(filename):
    """Read and display file contents by line."""
    try:
        with open(filename) as file_obj:
            lines = file_obj.readlines()
    except FileNotFoundError:
        print("File " + filename + " does not exist.")
    else:
        for line in lines:
            print(line.strip())

filenames = ['cats.txt', 'dogs.txt', 'fish.txt']
for filename in filenames:
    read_files(filename)
    print("")
#filename = 'cats.txt'
#read_files(filename)
