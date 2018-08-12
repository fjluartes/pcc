#!/usr/bin/env python
# players.py: working with part of a list
# 12 Aug 2018 | fjgl
# list_name[<start>, <end>]: slicing a list 
# end element not included (off by 1)
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:5])

# automatic start at beginning of list
print(players[:4])

# automatic end at end of list
print(players[2:])

# start from the right, to the end of list
print(players[-3:])

# looping through a slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
