#!/usr/bin/env python
# see_world.py: Exercises 3-8, 3-10
# 11 Aug 2018 | fjgl
# 3-8 Seeing The World
countries = ['Japan', 'US', 'UK', 'China', 'New Zealand']
print(countries)
print(sorted(countries))
print(countries)
print(sorted(countries, reverse=True))
print(countries)
countries.reverse()
print(countries)
countries.reverse()
print(countries)
countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)
print("\n")

# 3-10. Every Function
tech_companies = ['Microsoft', 'Amazon', 'Alphabet', 'Apple', 'Facebook']
print("Original list:")
print(tech_companies)
print("Sorted temp list:")
print(sorted(tech_companies))
print("Sorted temp list reverse:")
print(sorted(tech_companies, reverse=True))
print("List permanent reverse:")
tech_companies.reverse()
print(tech_companies)
print("List permanent sort:")
tech_companies.sort()
print(tech_companies)
print("List permanent sort in reverse:")
tech_companies.sort(reverse=True)
print(tech_companies)
print("List length:")
print(len(tech_companies))
print("Final list:")
print(tech_companies)
