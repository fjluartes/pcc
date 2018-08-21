#!/usr/bin/env python
# deli.py: Exercises 7-8, 7-9
# 21 Aug 2018 | fjgl
# 7-8. Deli
sandwich_orders = ['clubhouse', 'pastrami', 'tuna', 'chicken',
                   'pastrami', 'ham', 'pastrami']
finished_sandwiches = []

# 7-9. No Pastrami
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("Sandwiches that have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)
