#!/usr/bin/env python
# check_usernames.py: Exercise 5-10
# 16 Aug 2018 | fjgl
# 5-10. Check Usernames
current_users = ['Saitama', 'Genos', 'Sonic', 'Mumen rider', 'Bang']
new_users = ['Saitama', 'Genos', 'Tatsumaki', 'Atomic samurai']

for i in range(0, len(current_users)):
    temp = current_users.pop()
    current_users.insert(i, temp.lower())

for user in new_users:
    print(user)
    if user.lower() in current_users:
        print("That username is already taken.")
    else:
        print("That username is available.")
    print("")
