#!/usr/bin/env python
# number_reader.py: reading data using json.load()
# 1 Sep 2018 | fjgl
import json

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
