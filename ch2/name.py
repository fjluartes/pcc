#!/usr/bin/env python
# name.py: variables and string methods
# 11 Aug 2018 | fjgl
# changing string case
name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# string concatenation
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

# adding and stripping whitespace
name_r = name + "\n"
name_l = "\t" + name
print(name_r)
print(name_l)
print(name_r.rstrip())
print(name_l.lstrip())

# apostrophe
message = "One of Python's diverse strengths is its community."
print(message)
