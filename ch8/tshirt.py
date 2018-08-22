#!/usr/bin/env python
# tshirt.py: Exercises 8-3, 8-4
# 22 Aug 2018 | fjgl
def make_shirt(size='large', text='I love Python'):
    """Display size of shirt and message to be printed on shirt"""
    print("Size of shirt is " + size.title() +
          ", and text on shirt is \"" + text + "\".")
    
# 8-3. T-shirt
make_shirt('small', 'I\'m with stupid')
make_shirt(size='medium', text='Whitespaces FTW')
print("")

# 8-4. Large Shirts
make_shirt()
make_shirt(size='medium')
make_shirt(size='small', text='I love Javascript')
