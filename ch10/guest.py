#!/usr/bin/env python
# guest.py: Exercises 10-3, 10-4
# 29 Aug 2018 | fjgl
# 10-3. Guest
#filename = 'guest.txt'
#with open(filename, 'w') as file_object:
#    name = input("Enter your name: ")
#    file_object.write(name + '\n')

# 10-4. Guest Book
filename = 'guest_book.txt'
with open(filename, 'a') as file_object:
    while True:
        print("\nEnter 'q' to quit")
        name = input("Enter your name: ")
        if name == 'q':
            break
        else:
            print("\nHello, " + name.title() + "!")
        file_object.write(name.title() + '\n')
