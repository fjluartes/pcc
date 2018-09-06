#!/usr/bin/env python
# employee.py: Exercise 11-3
# 6 Sep 2018 | fjgl
class Employee():
    """A representation of employee, with name and salary."""
    def __init__(self, first, last, salary):
        """Initialize employee parameters."""
        self.full_name = first + ' ' + last
        self.salary = salary

    def give_raise(self, raise_amount=5000):
        """Adds a raise amount to the annual salary."""
        self.salary += raise_amount
