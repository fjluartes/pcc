#!/usr/bin/env python
# favorite_numbers.py: Exercises 10-11, 10-12
# 1 Sep 2018 | fjgl
import json

filename = 'favorite_numbers.json'
fave_number = input("What is your favorite number? ")
with open(filename, 'w') as f_obj:
    json.dump(fave_number, f_obj)
