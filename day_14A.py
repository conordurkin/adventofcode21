# Day 14 - inserting new values between values in a string. The catch is all
# insertions for a 'step' are supposed to be simultaneous - I think the trick is to
# write the insertions to a new string, instead of adding them to the initial string.
# Then I can use the new string as the input to the next 'step'.

import pandas as pd
import numpy as np
from collections import defaultdict, Counter

# Load the data, clean it up to get our string and a dictionary mapping for insertions.
data = pd.read_csv('data/day14.csv', header = None)
starting_string = data[0][0]
sequence = data[0][1:]

sequence_dict = defaultdict(list)
for entry in sequence:
    i,j = entry.split(' -> ')
    sequence_dict[i].append(j)

# This runs one 'step' - take the initial string, map the insertions, return new string.
def pair_insertion_step(start_template, mapping):
    output_sequence = ''
    for i in range(len(start_template)):
        input_pair = start_template[i:i+2]
        try:
            output = mapping[input_pair][0]
        except:
            output = ''
        output_sequence = output_sequence + start_template[i] + output
    return output_sequence

# This runs multiple steps (defaults to 1 if not specified)
def pair_insertion_loop(start_template_, mapping_, steps = 1):
    template_to_use = start_template_
    mapping_to_use = mapping_
    for i in range(steps):
        template_to_use = pair_insertion_step(template_to_use, mapping_to_use)
    return template_to_use

# Get our final output, count frequency of each element, find min and max
final_output = (pair_insertion_loop(starting_string, sequence_dict, 10))
counts = Counter(final_output)
min_element = min(counts, key = counts.get)
max_element = max(counts, key = counts.get)

# Find the difference between min and max and print it
print(counts[max_element] - counts[min_element])
