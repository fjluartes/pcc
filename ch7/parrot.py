#!/usr/bin/env python
# parrot.py: input() function, while loop
# 20 Aug 2018 | fjgl
prompt = "\nTell me something, and I'll repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# using a flag to determine program state
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
