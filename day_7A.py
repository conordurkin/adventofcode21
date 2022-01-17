# Day 7 - what's the min distance for the crabs?
# I understand the math, but man it is so counterintuitive to me that the mean isn't the min distance.

import pandas as pd
import numpy as np

data = pd.read_csv('data/day7.csv', header = None)
data = data.iloc[0].values.tolist()

# Find the min and max position of the crabs
floor = min(data)
ceiling = max(data)

# Try every possible position of the crabs. Save total distance down.
options = {}
for i in range(floor, ceiling + 1):
    travel_distance = 0
    for crab in data:
        travel_distance += abs(crab - i)

    options[i] = travel_distance

# Find the min total distance.
print(min(options.values()))
