#!/usr/bin/env python
# magicians.py: Exercise 8-9 to 8-11
# 23 Aug 2018 | fjgl
# 8-9. Magicians
def show_magicians(names):
    """Return the names of magicians in a list."""
    for name in names:
        message = "Welcome, " + name.title() + "!"
        print(message)

# 8-10. Great Magicians
def make_great(names, new_names):
    """Add 'The Great' to the list in magicians' names."""
    while names:
        current_name = names.pop()
        new_names.append('the great ' + current_name)

magicians = ['david blaine', 'harry houdini', 'david copperfield', 'criss angel']
great_magicians = []

# 8-11. Unchanged Magicians
#make_great(magicians , great_magicians)
make_great(magicians[:], great_magicians)
show_magicians(magicians)
print("")
show_magicians(great_magicians)
