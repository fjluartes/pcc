#!/usr/bin/env python
# fave_languages.py: nesting (lists in a dictionary)
# 19 Aug 2018 | fjgl
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
    }

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

# Don't nest list and dictionaries deeply.
