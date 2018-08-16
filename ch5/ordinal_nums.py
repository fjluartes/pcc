#!/usr/bin/env python
# ordinal_nums.py: Exercise 5-11
# 16 Aug 2018 | fjgl
# 5-11. Ordinal Numbers
nums = [i for i in range(1, 10)]

for num in nums:
    if num == 1:
        print(str(num) + "st")
    elif num == 2:
        print(str(num) + "nd")
    elif num == 3:
        print(str(num) + "rd")
    else:
        print(str(num) + "th")
