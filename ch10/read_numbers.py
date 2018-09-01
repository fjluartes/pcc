#!/usr/bin/env python
# read_numbers.py: Exercise 10-11
# 1 Sep 2018 | fjgl
import json

filename = 'favorite_numbers.json'
with open(filename) as f_obj:
    fave_number = json.load(f_obj)

print("I know your favorite number! It's " + fave_number + "!")
