#!/usr/bin/env python
# number_writer.py: storing data using json.dump()
# 1 Sep 2018 | fjgl
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
