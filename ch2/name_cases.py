#!/usr/bin/env python
# name_cases.py: Exercises 2-3 to 2-7
# 11 Aug 2018 | fjgl
# 2-3. Personal Message
name = "Eric"
print("Hello " + name + ", would you like to learn some Python today?")

# 2-4. name cases
print(name.lower())
print(name.upper())
print(name.title())

# 2-5, 2-6. Famous Quote
famous_person = 'Aristotle'
famous_quote = 'We are what we repeatedly do. Excellence then is not an act but a habit.'
message = famous_person + ' once said, "' + famous_quote + '"'
print(message)
famous_person = 'Albert Einstein'
famous_quote = 'A person who never made a mistake never tried anything new.'
message = famous_person + ' once said, "' + famous_quote + '"'
print(message)

# 2-7. Stripping Names
name2 = "\n\tRaymond\t\n"
print(name2)
print(name2.lstrip())
print(name2.rstrip())
print(name2.strip())
