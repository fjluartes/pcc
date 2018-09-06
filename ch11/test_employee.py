#!/usr/bin/env python
# test_employee.py: test employee class
# 6 Sep 2018 | fjgl
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test cases for employee.py."""
    def setUp(self):
        """Create employee for testing default and custom salaries."""
        first = 'jeff'
        last = 'bezos'
        self.salary = 100000
        self.employee = Employee(first, last, self.salary)

    def test_give_default_raise(self):
        """Test default raise for employee salary."""
        new_salary = self.employee.give_raise()
        self.assertEqual(self.salary + 5000, new_salary)

    def test_give_custom_raise(self):
        """Test custom raise for employee salary."""
        new_salary = self.employee.give_raise(10000)
        self.assertEqual(self.salary + 10000, new_salary)

unittest.main()
