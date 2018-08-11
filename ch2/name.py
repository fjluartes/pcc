#!/usr/bin/env python
# name.py: variables and string methods
# 11 Aug 2018 | fjgl
# upper(): convert string to uppercase
# lower(): convert string to lowercase
# title(): capitalize first letter of string
name = "ada Lovelace"
print(name.upper())
print(name.lower())
print(name.title())

# string concatenation
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name.title())

# adding and stripping whitespace
# rstrip(): remove whitespace at the right side of string
# lstrip(): remove whitespace at the left side of string
# strip(): remove whitespace at both sides
name_r = name + "\n"
name_l = "\t" + name
print(name_r)
print(name_l)
print(name_r.rstrip())
print(name_l.lstrip())
print(name_l.strip())

# apostrophe
message = "One of Python's diverse strengths is its community."
print(message)
