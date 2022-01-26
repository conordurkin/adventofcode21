# Syntax Scoring - good news, this one's solveable again!
# Basic approach - eliminate every pair of valid characters until I can't eliminate any more.
# Then find the first invalid 'closing' character (e.g. ')', '>', ']', '}') and get the score.

import pandas as pd
data = pd.read_csv('data/day10.csv', header = None)

# Function to find a closed set and eliminate them. Keep going until no more.
def reduce_row(row):
    i = 1
    while i == 1:
        if row.find('()') != -1:
            row = row.replace('()','')
        elif row.find('[]') != -1:
            row = row.replace('[]', '')
        elif row.find('<>') != -1:
            row = row.replace('<>', '')
        elif row.find('{}') != -1:
            row = row.replace('{}', '')
        else:
            i = 0
    return row

# Function to find the first bad character.
# First, reduce the row. Next, find the first bad character.
# Lastly, find the corresponding score for that character.
def find_bad_character(row):
    reduced_row = reduce_row(row)
    bad_paren = reduced_row.find(')')
    bad_brack = reduced_row.find(']')
    bad_brace = reduced_row.find('}')
    bad_arrow = reduced_row.find('>')
    bad_list = [bad_paren, bad_brack, bad_brace, bad_arrow]
    bad_list = [100 if bad == -1 else bad for bad in bad_list]
    if sum(bad_list) == 400:
        out = 0
    else:
        min_value = min(bad_list)
        min_location = bad_list.index(min_value)
        if min_location == 0:
            out = 3
        elif min_location == 1:
            out = 57
        elif min_location == 2:
            out = 1197
        elif min_location == 3:
            out = 25137
        else:
            out = 0
    return out

# Apply to the whole series.
outputs = data[0].apply(find_bad_character)

# Print sum. 
print(outputs.sum())
