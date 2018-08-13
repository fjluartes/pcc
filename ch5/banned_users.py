#!/usr/bin/env python
# banned_users.py: checking if a value is not in a list
# 13 Aug 2018 | fjgl
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

# boolean expressions
game_active = True
can_edit = False
print(game_active)
print(can_edit)
