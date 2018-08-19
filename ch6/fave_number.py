#!/usr/bin/env python
# fave_number.py: Exercise 6-2, 6-10
# 18 Aug 2018 | fjgl
# 6-2. Favorite Numbers
fave_num = {
    'red': [1, 3],
    'green': [2, 4, 6],
    'blue': [3],
    'yellow': [4, 1, 8],
    'pink': [5, 3, 8]
    }

#print("Red's favorite number is " + str(fave_num['red']) + ".")
#print("Green's favorite number is " + str(fave_num['green']) + ".")
#print("Blue's favorite number is " + str(fave_num['blue']) + ".")
#print("Yellow's favorite number is " + str(fave_num['yellow']) + ".")
#print("Pink's favorite number is " + str(fave_num['pink']) + ".")

# 6-10. Favorite Numbers
for name, numbers in fave_num.items():
    print(name.title() + "'s favorite numbers are:")
    for num in numbers:
        print("\t" + str(num))
