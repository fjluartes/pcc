#!/usr/bin/env python
# greet_user.py: saving and reading user-generated data
# 1 Sep 2018 | fjgl
import json

filename = 'username.json'
with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")
