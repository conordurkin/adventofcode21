import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore") # otherwise your output gives you a warning about the parser using "->" as a sep

data = pd.read_csv('data/day5.csv', header = None, sep = "->")

# Clean up the data file, give me four columns with start/end XY coordinates
starts = data[0].str.split(',', expand = True)
ends = data[1].str.split(',', expand = True)
combo = pd.concat([starts, ends], axis = 1)
combo.columns = ['start_x', 'start_y', 'end_x', 'end_y']
combo = combo.apply(pd.to_numeric)

# Remove the rows that aren't vertical or horizontal lines for part A.
combo['keep'] = np.where((combo.start_x == combo.end_x), 1, 0)
combo['keep'] = np.where((combo.start_y == combo.end_y), 1, combo['keep'])
small = combo.loc[combo.keep == 1].drop('keep', axis = 1).reset_index(drop = True)

# Get a list of every point that's covered by a given line.
points = []

for row in range(len(small)):
    entry = small.loc[row]

    if entry.start_x == entry.end_x:

        if entry.start_y < entry.end_y:
            for i in range(entry.start_y, (entry.end_y+1), 1):
                points.append((entry.start_x, i))

        else:
            for i in range(entry.start_y, (entry.end_y-1), -1):
                points.append((entry.start_x, i))

    elif entry.start_y == entry.end_y:

        if entry.start_x < entry.end_x:
            for i in range(entry.start_x, (entry.end_x+1), 1):
                points.append((i, entry.start_y))

        else:
            for i in range(entry.start_x, (entry.end_x-1), -1):
                points.append((i, entry.start_y))

    else:
        pass

# Convert that list into a series, summarize by frequency (value count), see how many appear more than once.
points_series = pd.Series(points)
summary = pd.DataFrame(points_series.value_counts())
print(len(summary.loc[summary[0] > 1]))
