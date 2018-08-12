#!/usr/bin/env python
# num_lists.py: Exercises 4-3 to 4-9
# 12 Aug 2018 | fjgl
# 4-3. Counting to Twenty
twenty = [value for value in range(1, 21)]
for num in twenty:
    print(num)
print("")

# 4-4. One Million
million = [value for value in range(1, 1000001)]
for num in million:
    print(num)
print("")

# 4-5. Summing a Million
print(sum(million))
print(min(million))
print(max(million))
print("")

# 4-6. Odd numbers
odd_twenty = list(range(1, 21, 2))
for num in odd_twenty:
    print(num)
print("")

# 4-7. Threes
threes = list(range(3, 31, 3))
for value in threes:
    print(value)
print("")

# 4-8. Cubes
cubes1 = []
for num in range(1, 11):
    cubes1.append(num**3)

for num in cubes1:
    print(num)
print("")

# 4-9. Cubes Comprehension
cubes2 = [value**3 for value in range(1, 11)]
print(cubes2)
