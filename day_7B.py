import pandas as pd
import numpy as np

data = pd.read_csv('data/day7.csv', header = None)
data = data.iloc[0].values.tolist()

# Find the min and max position of the crabs
floor = min(data)
ceiling = max(data)

# Function to define fuel cost
def fuel_calc(dist):
    fuel = 0
    for i in range(dist+1):
        fuel += i
    return fuel


# Try every possible position of the crabs. Save total distance down.
options = {}
for i in range(floor, ceiling + 1):
    travel_distance = 0
    for crab in data:
        travel_distance += fuel_calc(abs(crab - i))

    options[i] = travel_distance

# Find the min total distance.
print(min(options.values()))

# Note: It's not great to have the fuel_calc function re-run for every single iteration.
# A more elegant / efficient solution would be to use the floor/ceiling to find the max possible distance, find the fuel cost for
# each distance exactly once and store that information in a dictionary, and then lookup the proper cost per crab in the "for crab in data" step (line 24).
# However, I am lazy. 
