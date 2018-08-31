#!/usr/bin/env python
# addition.py: Exercise 10-6, 10-7
# 31 Aug 2018 | fjgl
print("Add two integers.")
print("Enter 'q' to quit.")
while True:
    first_num = input("\nEnter first number: ")
    if first_num == 'q':
        break
    second_num = input("Enter second number: ")
    if second_num == 'q':
        break
    try:
        first_num = int(first_num)
        second_num = int(second_num)
    except ValueError:
        print("You must enter a number!")
    else:
        answer = first_num + second_num
        print(str(first_num) + " + " + str(second_num) + " = " + str(answer))
