import pandas as pd
import numpy as np

data = pd.read_csv('day6.csv', header = None)

school_of_fish = data.iloc[0].values.tolist()

for day in range(80):
    new_school = [] # Put the "New fish" in a different list and append at the end of each day, so they don't get touched til tomorrow.
    for oldfish in school_of_fish:
        fish = school_of_fish.pop(0) # Need to pop the first entry, not last one, or we just keep popping / appending the same fish repeatedly.
        if fish == 0:
            new_school.append(8)
            school_of_fish.append(6)

        else:
            fish -= 1
            school_of_fish.append(fish)

    for each in new_school:
        school_of_fish.append(each)

print(len(school_of_fish))
