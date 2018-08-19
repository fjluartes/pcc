#!/usr/bin/env python
# glossary.py: Exercise 6-3, 6-4
# 18 Aug 2018 | fjgl
# 6-3, 6-4. Glossary
# print, list, for, if, dictionary
glossary = {
    'print': 'Python keyword used to display data. (usually strings)',
    'list': 'A collection of items in a particular order.',
    'for': 'Python keyword used to loop into a list, tuple, or dictionary.',
    'if': 'Python keyword for conditional statements.',
    'dictionary': 'A collection of key-value pairs.',
    'tuple': 'A list whose items cannot be modified.',
    'del': 'Python keyword for removing an item in a list permanently.',
    'and': 'Python keyword for two statements that must be both true.',
    'or': 'Python keyword for two statements that at least one must be true.',
    'not': 'Python keyword for negating a conditional statement.'
    }

for word, definition in glossary.items():
    print(word + ": " + definition)
