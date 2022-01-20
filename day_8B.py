# Wow, this one was hard. Really had to think through the logic of how exactly to solve it, and how to code.
# Plus side - I got to code a few functions for the first time in this project, and actually used df.apply(FUNCTION) instead of lazily using for loops.

# Of the ten possible numbers used, four had unique lengths (from part A) - 1, 4, 7, 8.
# The trick is to use those specific strings to identify the others.
# Three numbers have a string length of six - those are 6, 9, and 0.
# Of those, 9 contains the string for 1 and for 4. 0 contains the string for 1 but not 4, and 6 contains neither.
# Three numbers have a string length of five - those are 3, 5, and 2. 3 is the only one which contains the strings for 1.
# 5 is difficult... it contains the "difference" between 7 and 4 (this is basically the 'top half' of 5)

# So the trick is to identify the strings for 1,4,7,8, store those, then loop over all the entries and
# figure out which ones contain the right strings to be a given number.

# Then I store those numbers and combine them to get my output code.
# Then I sum that list of numbers.

import pandas as pd
import numpy as np

data = pd.read_csv('data/day8.csv', header = None, sep = " ")

# This is a function to check whether a given string contains all of a set of entries (e.g. are A, B, C all in 'ABCDE').
# It's how I check if a string contains another string (e.g. "does this contain the string for 1 and 4?")
def segment_checker(string_to_check, set_to_find):
    for letter in set_to_find:
        if string_to_check.find(letter) == -1:
            out = False
            break
        else:
            pass
        out = True
    return out

# This is the function to solve a given row.
def row_solver(series):
    inputs = series[0:10]

    # Figure out the entries for 1, 4, 7, 8, plus the 'difference' between 1 and 4 (the top half of 5)
    set_1 = set([x for x in inputs if len(x) == 2].pop())
    set_4 = set([x for x in inputs if len(x) == 4].pop())
    set_7 = set([x for x in inputs if len(x) == 3].pop())
    set_8 = set([x for x in inputs if len(x) == 7].pop())
    set_5head = set_4.symmetric_difference(set_7)

    outputs = series[11:]
    decoded_output = []

    # Okay, now loop over the four outputs
    for entry in outputs:
        if len(entry) == 2:
            out = 1
        elif len(entry) == 4:
            out = 4
        elif len(entry) == 3:
            out = 7
        elif len(entry) == 7:
            out = 8
        elif len(entry) == 5:
            if segment_checker(entry, set_1) == True:
                out = 3
            elif segment_checker(entry, set_5head) == True:
                out = 5
            else:
                out = 2
        elif len(entry) == 6:
            if segment_checker(entry, set_1) == False:
                out = 6
            elif segment_checker(entry, set_4) == False:
                out = 0
            else:
                out = 9
        else:
            pass

        decoded_output.append(out)

    # Turn the four output digits into a four digit number (kinda hacky but whatever)
    row_result = 1000 * decoded_output[0] + 100 * decoded_output[1] + 10 * decoded_output[2] + decoded_output[3]
    return row_result

# Apply this function to each row of the dataset
outputs = data.apply(row_solver, axis = 1)

# Sum the outputs and print the answer. 
print(outputs.sum())
