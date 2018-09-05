#!/usr/bin/env python
# test_city_functions.py: Exercise 11-1 (test cases for city_functions)
# 4 Sep 2018 | fjgl
import unittest
from city_functions import get_formatted_city

class CitiesTestCase(unittest.TestCase):
    """Test cases for 'city_functions.py'."""
    def test_city_country(self):
        """Do cities like 'Santiago, Chile' work?"""
        formatted_city = get_formatted_city('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do cities like 'Santiago, Chile - population 5000000' work?"""
        formatted_city = get_formatted_city('santiago', 'chile', population=5000000)
        self.assertEqual(formatted_city, 'Santiago, Chile - Population 5000000')

unittest.main()
