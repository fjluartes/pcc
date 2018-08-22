#!/usr/bin/env python
# formatted_name.py: return a simple value
# 22 Aug 2018 | fjgl
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

# with optional middle_name
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
musician = get_formatted_name('jimi', 'hendrix')
print(musician)