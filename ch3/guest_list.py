#!/usr/bin/env python
# guest_list.py: Exercises 3-4 to 3-7, 3-9
# 11 Aug 2018 | fjgl
# 3-4. Guest List
guest_list = ['Benjamin Franklin', 'Alan Turing', 'Donald Knuth']
for guest in guest_list:
    print(guest + ", you are invited by me for a sumptuous dinner.")
print(str(len(guest_list)) + " guests are invited.\n")

# 3-5. Changing Guest List
cant_make_it = guest_list.pop(1)
print(cant_make_it + " can't make it to the dinner.\n")
new_guest = 'Robert Floyd'
guest_list.insert(1, new_guest)
for guest in guest_list:
    print(guest + ", you are invited by me for a sumptuous dinner.")
print(str(len(guest_list)) + " guests are invited.\n")

# 3-6. More Guests
new_guests = ['Bill Gates', 'John Carmack', 'Ryan Dahl']
guest_list.insert(0, new_guests[0])
guest_list.insert(2, new_guests[1])
guest_list.append(new_guests[2])
for guest in guest_list:
    print(guest + ", you are invited by me for a sumptuous dinner.")
print(str(len(guest_list)) + " guests are invited.\n")

# 3-7. Shrinking Guest List
not_invited = guest_list.pop()
print("Sorry " + not_invited + ", I can't invite you to dinner.")

not_invited = guest_list.pop()
print("Sorry " + not_invited + ", I can't invite you to dinner.")

not_invited = guest_list.pop()
print("Sorry " + not_invited + ", I can't invite you to dinner.")

not_invited = guest_list.pop()
print("Sorry " + not_invited + ", I can't invite you to dinner.")

for guest in guest_list:
    print(guest + ", you're still invited to dinner.")
print(str(len(guest_list)) + " guests are invited.")
del guest_list[-1]
del guest_list[-1]
print(guest_list)

# 3-9. Dinner Guests
# str(len(guest_list))

# 3-11. Intentional Error
# print(guest_list[-1])
