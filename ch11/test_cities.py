#!/usr/bin/env python
# test_city_functions.py: Exercise 11-1 (test cases for city_functions)
# 4 Sep 2018 | fjgl
import unittest
from city_functions import get_formatted_city

class CitiesTestCase(unittest.TestCase):
    """Test cases for 'city_functions.py'."""
    def test_city_country(self):
        """Do cities like 'Paris, France' work?"""
        formatted_city = get_formatted_city('paris', 'france')
        self.assertEqual(formatted_city, 'Paris, France')

unittest.main()
