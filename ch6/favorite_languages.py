#!/usr/bin/env python
# favorite_languages.py: dictionary of similar objects
# 18 Aug 2018 | fjgl
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }

#print("Sarah's favorite language is " +
#      favorite_languages['sarah'].title() +
#      ".")

# loop through favorite_languages dictionary
#for name, language in favorite_languages.items():
#    print(name.title() + "'s favorite language is " +
#          language.title() + ".")

# looping through all keys (default behavior when looping dict)
#for name in favorite_languages.keys():
#    print(name.title())
#for name in favorite_languages:
#    print(name.title())

# accessing values using keys in a loop
#friends = ['phil', 'sarah']
#for name in favorite_languages.keys():
#    print(name.title())
#    if name in friends:
#        print("  Hi " + name.title() +
#              ", I see your favorite language is " +
#              favorite_languages[name].title() + "!")

# keys() return the list of keys
# check if an element is not in the list of keys
#if 'erin' not in favorite_languages.keys():
#    print("Erin, please take our poll!")

# looping through a dictionary in order
#for name in sorted(favorite_languages.keys()):
#    print(name.title() + ", thank you for taking our poll.")

# looping through all values
#for language in favorite_languages.values():
#    print(language.title())

# set(): similar to a list but items must be unique
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
