#!/usr/bin/env python
# pi_string.py: working with file's contents
# 29 Aug 2018 | fjgl
#filename = 'pi_digits.txt'
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

# pi_million_digits
#print(pi_string[:52] + "...")
#print(len(pi_string))

# birthday in pi
birthday = input("Enter your birthday in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday des not appear in the first million digits of pi!")
