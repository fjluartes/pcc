#!/usr/bin/env python
# rivers.py: Exercise 6-5
# 19 Aug 2018 | fjgl
# 6-5. Rivers
rivers = {
    'amazon': 'brazil',
    'nile': 'egypt',
    'yangtze': 'china'
    }

for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")
print("")
    
for river in rivers.keys():
    print(river.title())
print("")

for country in rivers.values():
    print(country.title())
print("")
