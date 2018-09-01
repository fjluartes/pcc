#!/usr/bin/env python
# remember_me.py: saving and reading user-generated data
# 1 Sep 2018 | fjgl
import json

username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")
