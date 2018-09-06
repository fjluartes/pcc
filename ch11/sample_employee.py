#!/usr/bin/env python
# sample_employee.py: call employee class
# 6 Sep 2018 | fjgl
from employee import Employee

print("\nEnter 'q' at any time to quit.")
while True:
    first = input("\nEnter first name: ")
    if first == 'q':
        break
    last = input("Enter last name: ")
    if last == 'q':
        break
    salary = input("Enter salary: ")
    if salary == 'q':
        break
    employee = Employee(first, last, int(salary))
    print("\nEmployee Name: " + employee.full_name.title())
    print("Salary: " + str(employee.salary))
    raise_choice = input("Do you want to give " + employee.full_name.title() +
                      " a raise? (yes/no) ")
    if raise_choice.lower() == 'yes':
        d = input("Do you want to give the default raise or not? (yes/no) ")
        if d.lower() == 'yes':
            employee.give_raise()
            print("New Salary: " + str(employee.salary))
        else:
            raise_amt = input("Enter raise amount: ")
            employee.give_raise(int(raise_amt))
            print("New Salary: " + str(employee.salary))
    else:
        print("Salary: " + str(employee.salary))
