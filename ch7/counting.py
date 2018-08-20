#!/usr/bin/env python
# counting.py: while loop, using continue in a loop
# 20 Aug 2018 | fjgl
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
print("")
    
# infinite loop if line 16 is removed
x = 1
while x <= 5:
    print(x)
    x += 1
