#!/usr/bin/env python
# common_words.py: Exercise 10-10
# 31 Aug 2018 | fjgl
def count_specific_word(word, filename):
    """Count the number of specific word in a file."""
    total = 0
    try:
        with open(filename) as file_obj:
            lines = file_obj.readlines()
    except FileNotFoundError:
        print("\nFile " + filename + " does not exist.")
    else:
        for line in lines:
            nline = line.lower()
            word_count = nline.count(word.lower())
            total += word_count
        print("\nText: " + filename)
        print("Number of '" + word + "' in text: " + str(total))

filenames = ['count_of_monte_cristo.txt', 'siddhartha.txt', 'little_women.txt']
for filename in filenames:
    count_specific_word('the', filename)
